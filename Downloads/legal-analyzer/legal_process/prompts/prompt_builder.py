from typing import Dict, Any
import json


class PromptBuilder:
    """Class để tạo prompt phân tích quan hệ văn bản"""
    
    @staticmethod
    def create_van_ban_relation_prompt(van_ban_a: Dict[str, Any]):
        """
        Tạo prompt để phân tích quan hệ văn bản-văn bản

        Args:
            van_ban_a: Dữ liệu văn bản A
        Returns:
            Prompt string cho quan hệ văn bản
        """

        prompt = f"""
            Bạn là chuyên gia phân tích văn bản pháp luật Việt Nam. Nhiệm vụ của bạn là phân tích quan hệ VĂN BẢN-VĂN BẢN trong 1 văn bản sau

            === VĂN BẢN A ===
            - Số hiệu: {van_ban_a.get('so_hieu_vb', '')}
            - Tên đầy đủ: {van_ban_a.get('ten_day_du', '')}
            - Cơ quan ban hành: {van_ban_a.get('co_quan_ban_hanh', '')}
            - Ngày ban hành: {van_ban_a.get('ngay_ban_hanh', '')}
            - Loại văn bản: {van_ban_a.get('loai_van_ban', '')}

            Căn cứ pháp lý:
            {json.dumps(van_ban_a.get('can_cu', []), ensure_ascii=False, indent=2)}

            === NHIỆM VỤ PHÂN TÍCH QUAN HỆ VĂN BẢN ===

            Hãy phân tích và tạo ra kết quả JSON theo định dạng sau:

            {{
            "van_ban_goc": {{
                "so_hieu_vb": "Số hiệu văn bản goc",
                "ten_day_du": "Tên đầy đủ văn bản goc",
                "co_quan_ban_hanh": "Cơ quan ban hành ",
                "ngay_ban_hanh": "Ngày ban hành ",
                "loai_van_ban": "Loại văn bản "
            }},
            "quan_he_van_ban": [
                {{
                "loai_quan_he": "Bãi bỏ|Bản dịch|Căn cứ|Dẫn chiếu|Đình chỉ thi hành|Đính chính|Hợp nhất|Hướng dẫn áp dụng|Quy định, hướng dẫn chi tiết|Sửa đổi, bổ sung|Tạm ngưng hiệu lực|Thay thế",
                "van_ban_nguon": {{
                    "so_hieu_vb": "Số hiệu văn bản nguồn",
                    "ten_day_du": "Tên văn bản nguồn"
                }},
                "van_ban_dich": {{
                    "so_hieu_vb": "Số hiệu văn bản đích",
                    "ten_day_du": "Tên văn bản đích"
                }}
            ]}}
            }}

            === QUY TẮC PHÂN TÍCH QUAN HỆ VĂN BẢN ===

            **CÁC LOẠI QUAN HỆ VĂN BẢN:**
            1. **Căn cứ**: Văn bản A dựa trên văn bản B để ban hành
            2. **Sửa đổi, bổ sung**: Văn bản A sửa đổi điều khoản của văn bản B
            3. **Thay thế**: Văn bản A thay thế hoàn toàn văn bản B
            4. **Bãi bỏ**: Văn bản A bãi bỏ văn bản B
            5. **Hướng dẫn áp dụng**: Văn bản A hướng dẫn thực hiện văn bản B
            6. **Dẫn chiếu**: Văn bản A tham chiếu đến văn bản B
            7. **Quy định, hướng dẫn chi tiết**: Văn bản A quy định chi tiết văn bản B
            8. **Đính chính**: Văn bản A đính chính văn bản B
            9. **Hợp nhất**: Văn bản A hợp nhất văn bản B
            10. **Đình chỉ thi hành**: Văn bản A đình chỉ thi hành văn bản B
            11. **Tạm ngưng hiệu lực**: Văn bản A tạm ngưng hiệu lực văn bản B
            12. **Bản dịch**: Văn bản A là bản dịch của văn bản B

            **CÁCH PHÂN TÍCH:**
            - Xem xét căn cứ pháp lý và tên đầy đủ của văn bản ( ví dụ căn cứ hiến pháp là quan hệ văn bản với hiến pháp)
            - Tìm từ khóa chỉ quan hệ: "căn cứ vào", "sửa đổi", "bổ sung", "thay thế", "bãi bỏ"
            - So sánh ngày ban hành để xác định văn bản nào ban hành trước/sau
            - Xem xét nội dung và mục đích của văn bản

            **LƯU Ý:**
            - Chỉ trả về JSON hợp lệ, không có text thừa
            - Phân tích kỹ căn cứ pháp lý để tìm quan hệ
            - Ưu tiên quan hệ rõ ràng và có bằng chứng cụ thể
            - Nếu không có quan hệ rõ ràng, trả về mảng quan_he_van_ban rỗng

            Hãy phân tích và trả về kết quả:
            """
        return prompt