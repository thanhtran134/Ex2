from typing import Dict, Any, Optional
import json
import re
from openai import OpenAI

from legal_process.prompts.prompt_builder import PromptBuilder
from legal_process.templates.vanban import VanBan, VanBanRelationResult
from legal_process.config import Config


class VanBanAnalyzer:
    """Service để phân tích quan hệ văn bản pháp luật"""
    
    def __init__(self, config: Optional[Config] = None):
        """
        Khởi tạo VanBanAnalyzer
        
        Args:
            config: Cấu hình cho analyzer
        """
        self.config = config or Config()
        self.client = OpenAI(
            api_key=self.config.API_KEY,
            base_url=self.config.BASE_URL
        )
        self.prompt_builder = PromptBuilder()
    
    def analyze_relation(
        self, 
        van_ban_a: Dict[str, Any], 
    ) -> Dict[str, Any]:
        """
        Phân tích quan hệ giữa hai văn bản
        
        Args:
            van_ban_a: Dữ liệu văn bản A
            
        Returns:
            Kết quả phân tích quan hệ văn bản
        """
        prompt = self.prompt_builder.create_van_ban_relation_prompt(
            van_ban_a
        )
        
        try:
            response = self.client.chat.completions.create(
                model=self.config.MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": self.config.SYSTEM_PROMPT
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=self.config.TEMPERATURE,
                max_tokens=self.config.MAX_TOKENS,
            )
            
            result_text = response.choices[0].message.content.strip()
            
            # Parse JSON từ response
            json_match = re.search(r'\{.*\}', result_text, re.DOTALL)
            if json_match:
                result = json.loads(json_match.group())
                return result
            else:
                return {
                    "error": "Không thể parse JSON từ response", 
                    "raw_response": result_text
                }
                
        except Exception as e:
            return {"error": f"Lỗi khi gọi LLM: {str(e)}"}
    