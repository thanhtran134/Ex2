
import os
from typing import Optional


class Config:
    """Cấu hình cho VanBanAnalyzer"""
    
    def __init__(self):
        """Config llm"""
        self.API_KEY = os.getenv('OPENAI_API_KEY', 'EMPTY')
        self.BASE_URL = os.getenv('OPENAI_BASE_URL', 'http://124.197.20.172:3333/v1')
        self.MODEL_NAME = os.getenv('MODEL_NAME', 'Qwen/Qwen3-8B')
        self.TEMPERATURE = float(os.getenv('TEMPERATURE', '0.1'))
        self.MAX_TOKENS = int(os.getenv('MAX_TOKENS', '4000'))
        
        self.SYSTEM_PROMPT = (
            "Bạn là chuyên gia phân tích văn bản pháp luật Việt Nam. "
            "Trả về kết quả dưới dạng JSON hợp lệ, không có text thừa. "
            "Bạn phải trả quan hệ về giữa 2 văn bản"
        )
    
    def validate(self) -> bool:
        """Kiểm tra cấu hình có hợp lệ không"""
        if not self.API_KEY or self.API_KEY == 'EMPTY':
            raise ValueError("API_KEY not null")
        return True