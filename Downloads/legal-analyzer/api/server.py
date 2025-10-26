from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict, Any, Optional, List
import json
import uvicorn
import logging

from legal_process.services.legal_doc_analyzer import VanBanAnalyzer
from legal_process.config import Config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Relationship Analyzer for Vietnamese Legal Documents",
    description="Analyzing Vietnamese legal document relations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize analyzer
config = Config()
try:
    config.validate()
    analyzer = VanBanAnalyzer(config)
    logger.info("VanBanAnalyzer initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize analyzer: {e}")
    analyzer = None


# Pydantic models
class VanBanInput(BaseModel):
    """Model cho input văn bản"""
    so_hieu_vb: Optional[str] = ""
    so_hieu: Optional[str] = ""
    ten_day_du: str
    co_quan_ban_hanh: str
    ngay_ban_hanh: str
    loai_van_ban: str


class AnalyzeRequest(BaseModel):
    """Model cho request phân tích"""
    van_ban_a: Dict[str, Any]


class HealthResponse(BaseModel):
    """Model cho health check response"""
    status: str
    version: str
    analyzer_ready: bool


class ErrorResponse(BaseModel):
    """Model cho error response"""
    error: str
    detail: Optional[str] = None


@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint"""
    return {
        "message": "Van Ban Analyzer API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if analyzer else "unhealthy",
        "version": "1.0.0",
        "analyzer_ready": analyzer is not None
    }


@app.post("/api/v1/analyze", response_model=Dict[str, Any])
async def analyze_relations(request: AnalyzeRequest):
    """
    Phân tích quan hệ giữa hai văn bản
    
    Args:
        request: AnalyzeRequest chứa thông tin hai văn bản
        
    Returns:
        Kết quả phân tích quan hệ văn bản
    """
    if not analyzer:
        raise HTTPException(
            status_code=503,
            detail="Analyzer service is not available"
        )
    
    try:
        logger.info("Received analysis request")
        logger.info(f"Van ban: {request.get('so_hieu_vb', 'N/A')}")

        result = analyzer.analyze_relation(
            request.van_ban_a)
        
        # Check for errors in result
        if "error" in result:
            logger.error(f"Analysis error: {result['error']}")
            raise HTTPException(
                status_code=500,
                detail=result.get('error', 'Unknown error')
            )
        
        logger.info("Analysis completed successfully")
        return result
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )


@app.get("/api/v1/relation-types", response_model=List[Dict[str, str]])
async def get_relation_types():
    """
    Lấy danh sách các loại quan hệ văn bản
    
    Returns:
        List các loại quan hệ văn bản
    """
    return [
        {"code": "can_cu", "name": "Căn cứ", "description": "Văn bản A dựa trên văn bản B để ban hành"},
        {"code": "sua_doi_bo_sung", "name": "Sửa đổi, bổ sung", "description": "Văn bản A sửa đổi điều khoản của văn bản B"},
        {"code": "thay_the", "name": "Thay thế", "description": "Văn bản A thay thế hoàn toàn văn bản B"},
        {"code": "bai_bo", "name": "Bãi bỏ", "description": "Văn bản A bãi bỏ văn bản B"},
        {"code": "huong_dan_ap_dung", "name": "Hướng dẫn áp dụng", "description": "Văn bản A hướng dẫn thực hiện văn bản B"},
        {"code": "dan_chieu", "name": "Dẫn chiếu", "description": "Văn bản A tham chiếu đến văn bản B"},
        {"code": "quy_dinh_chi_tiet", "name": "Quy định, hướng dẫn chi tiết", "description": "Văn bản A quy định chi tiết văn bản B"},
        {"code": "dinh_chinh", "name": "Đính chính", "description": "Văn bản A đính chính văn bản B"},
        {"code": "hop_nhat", "name": "Hợp nhất", "description": "Văn bản A hợp nhất văn bản B"},
        {"code": "dinh_chi_thi_hanh", "name": "Đình chỉ thi hành", "description": "Văn bản A đình chỉ thi hành văn bản B"},
        {"code": "tam_ngung_hieu_luc", "name": "Tạm ngưng hiệu lực", "description": "Văn bản A tạm ngưng hiệu lực văn bản B"},
        {"code": "ban_dich", "name": "Bản dịch", "description": "Văn bản A là bản dịch của văn bản B"}
    ]


if __name__ == "__main__":
    uvicorn.run(
        "api.server:app",
        host="0.0.0.0",
        port=8686,
        reload=True,
        log_level="info"
    )