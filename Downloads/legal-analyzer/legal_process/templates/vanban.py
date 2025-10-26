from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class VanBan:
    """Model cho văn bản pháp luật"""
    uuid: Optional[str] = None
    so_hieu_vb: str = ""
    ten_day_du: str = ""
    co_quan_ban_hanh: str = ""
    ngay_ban_hanh: str = ""
    loai_van_ban: str = ""
    can_cu: List[Dict[str, Any]] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'VanBan':
        """Tạo VanBan từ dictionary"""
        return cls(
            so_hieu_vb=data.get('so_hieu_vb', data.get('so_hieu', '')),
            ten_day_du=data.get('ten_day_du', ''),
            co_quan_ban_hanh=data.get('co_quan_ban_hanh', ''),
            ngay_ban_hanh=data.get('ngay_ban_hanh', ''),
            loai_van_ban=data.get('loai_van_ban', ''),
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Chuyển VanBan thành dictionary"""
        return {
            'so_hieu_vb': self.so_hieu_vb,
            'ten_day_du': self.ten_day_du,
            'co_quan_ban_hanh': self.co_quan_ban_hanh,
            'ngay_ban_hanh': self.ngay_ban_hanh,
            'loai_van_ban': self.loai_van_ban
        }


@dataclass
class QuanHeVanBan:
    """Model cho quan hệ văn bản"""
    uuid: str
    loai_quan_he: str
    van_ban_nguon: Dict[str, Any]
    van_ban_dich: Dict[str, Any]
    
    def to_dict(self) -> Dict[str, Any]:
        """Chuyển QuanHeVanBan thành dictionary"""
        return {
            'uuid': self.uuid,
            'loai_quan_he': self.loai_quan_he,
            'van_ban_nguon': self.van_ban_nguon,
            'van_ban_dich': self.van_ban_dich
        }


@dataclass
class VanBanRelationResult:
    """Model cho kết quả phân tích quan hệ văn bản"""
    van_ban_a: Dict[str, Any]
    quan_he_van_ban: List[Dict[str, Any]] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        """Chuyển kết quả thành dictionary"""
        return {
            'van_ban_a': self.van_ban_a,
            'quan_he_van_ban': self.quan_he_van_ban
        }