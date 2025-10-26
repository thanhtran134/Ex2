"""Van Ban Analyzer - Phân tích quan hệ văn bản pháp luật Việt Nam"""

__version__ = "1.0.0"

from legal_process.services.legal_doc_analyzer import VanBanAnalyzer
from legal_process.config import Config

__all__ = ['VanBanAnalyzer', 'Config']
