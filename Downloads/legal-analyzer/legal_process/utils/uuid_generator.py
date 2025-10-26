import hashlib
import uuid
from typing import Dict, Any


class UUIDGenerator:
    """Utility class để tạo UUID cho văn bản"""
    
    @staticmethod
    def generate_van_ban_uuid(van_ban_data: Dict[str, Any]) -> str:
        """
        Tạo UUID cho văn bản dựa trên thông tin văn bản
        
        Args:
            van_ban_data: Dictionary chứa thông tin văn bản
            
        Returns:
            UUID string
        """
        so_hieu_vb = van_ban_data.get('so_hieu_vb', van_ban_data.get('so_hieu', ''))
        ngay_ban_hanh = van_ban_data.get('ngay_ban_hanh', '')
        ten_day_du = van_ban_data.get('ten_day_du', '')
        
        content = f"{so_hieu_vb}_{ngay_ban_hanh}_{ten_day_du}"
        hash_obj = hashlib.md5(content.encode('utf-8'))
        hash_hex = hash_obj.hexdigest()
        
        uuid_obj = uuid.UUID(hash_hex)
        return str(uuid_obj)
    
    @staticmethod
    def generate_random_uuid() -> str:
        """Tạo UUID ngẫu nhiên"""
        return str(uuid.uuid4())