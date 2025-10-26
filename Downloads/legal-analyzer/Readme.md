# Van Ban Analyzer

Hệ thống phân tích quan hệ văn bản pháp luật Việt Nam sử dụng LLM với REST API.

## 📁 Cấu trúc thư mục

```
van-ban-analyzer/
├── van_ban_analyzer/           # Package chính
│   ├── __init__.py
│   ├── config.py              # Cấu hình hệ thống
│   ├── models/                # Data models
│   │   ├── __init__.py
│   │   └── van_ban.py
│   ├── services/              # Business logic
│   │   ├── __init__.py
│   │   └── analyzer.py
│   ├── prompts/               # Prompt templates
│   │   ├── __init__.py
│   │   └── prompt_builder.py
│   └── utils/                 # Utilities
│       ├── __init__.py
│       └── uuid_generator.py
├── api/                       # REST API
│   ├── __init__.py
│   └── server.py             # FastAPI server
├── data/                      # Thư mục chứa file input
│   └── .gitkeep
├── output/                    # Thư mục chứa kết quả
│   └── .gitkeep
├── main.py                    # CLI entry point
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose configuration
├── start_api.sh              # Script khởi động API
├── run.sh                     # Script chạy CLI
├── test_api.sh               # Script test API
├── .env.example              # Environment variables template
├── .gitignore
├── README.md
└── API_EXAMPLES.md           # API usage examples
```

## 🚀 Cài đặt

### Yêu cầu

- Python 3.10+
- Docker & Docker Compose (nếu chạy với Docker)
- OpenAI API key hoặc compatible API endpoint

### Cài đặt Local

1. Clone repository:
```bash
git clone <repository-url>
cd van-ban-analyzer
```

2. Tạo file `.env` từ template:
```bash
cp .env.example .env
```

3. Cập nhật thông tin trong `.env`:
```bash
OPENAI_API_KEY=your-api-key-here
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=Qwen/Qwen3-8B
```

4. Tạo virtual environment và cài đặt dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### Cài đặt với Docker

1. Clone repository và tạo file `.env` như trên

2. Build Docker image:
```bash
docker-compose build
```

## 💻 Sử dụng

### Option 1: REST API (Recommended)

#### Khởi động API Server

**Local:**
```bash
docker-compose build
./run.sh local
```

**Docker:**
```bash
./run.sh docker
```

API sẽ chạy tại: `http://localhost:8585`
- Documentation: `http://localhost:8585/docs`
- Health check: `http://localhost:8585/health`

#### Test API

```bash
chmod +x test_api.sh
./test_api.sh http://localhost:8585
```

#### Sử dụng API

**1. Health Check:**
```bash
curl http://localhost:8000/health
```

**2. Phân tích với JSON body:**
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "van_ban_a": {...}
  }'
```

**3. Phân tích với file upload:**
```bash
curl -X POST http://localhost:8000/api/v1/analyze/upload \
  -F "van_ban_a=@data/van_ban_a.json"
```

**4. Lấy danh sách loại quan hệ:**
```bash
curl http://localhost:8000/api/v1/relation-types
```

Xem thêm examples tại [API_EXAMPLES.md](API_EXAMPLES.md)

### Option 2: CLI

#### Chạy Local

```bash
# Cách 1: Sử dụng script run.sh
chmod +x run.sh
./run.sh local data/van_ban_a.json data/van_ban_b.json output/result.json

# Cách 2: Chạy trực tiếp
source venv/bin/activate
python main.py --van-ban-a data/van_ban_a.json \
               --output output/result.json
```

#### Chạy với Docker

```bash
# Sử dụng script run.sh
./run.sh docker data/van_ban_a.json data/van_ban_b.json output/result.json

# Hoặc sử dụng docker-compose trực tiếp
docker-compose run --rm van-ban-analyzer-api python main.py \
    --van-ban-a /app/data/van_ban_a.json \
    --output /app/output/result.json
```

## 📝 API Endpoints

| Method | Endpoint | Mô tả |
|--------|----------|-------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/api/v1/relation-types` | Danh sách loại quan hệ |
| POST | `/api/v1/analyze` | Phân tích với JSON body |
| POST | `/api/v1/analyze/upload` | Phân tích với file upload |

## 📋 Định dạng Input

File JSON input phải có cấu trúc:

```json
{
  "so_hieu_vb": "28/2009/TT-BCT",
  "ten_day_du": "Tên đầy đủ văn bản",
  "co_quan_ban_hanh": "Bộ Công Thương",
  "ngay_ban_hanh": "2009-07-15",
  "loai_van_ban": "Thông tư",
}
```

## 📤 Định dạng Output

```json
{
  "van_ban_a": {
    "so_hieu_vb": "...",
    "ten_day_du": "...",
    "co_quan_ban_hanh": "...",
    "ngay_ban_hanh": "...",
    "loai_van_ban": "..."
  },
  "van_ban_b": {
    "so_hieu_vb": "...",
    ...
  },
  "quan_he_van_ban": [
    {
      "loai_quan_he": "Căn cứ",
      "van_ban_nguon": {
        "so_hieu_vb": "...",
        "ten_day_du": "..."
      },
      "van_ban_dich": {
        "so_hieu_vb": "...",
        "ten_day_du": "..."
      }
    }
  ]
}
```

## 🔧 Cấu hình

Các biến môi trường trong `.env`:

| Biến | Mô tả | Mặc định |
|------|-------|----------|
| `OPENAI_API_KEY` | API key | (bắt buộc) |
| `OPENAI_BASE_URL` | Base URL của API | https://api.openai.com/v1 |
| `MODEL_NAME` | Tên model | Qwen/Qwen3-8B |
| `TEMPERATURE` | Temperature cho LLM | 0.1 |
| `MAX_TOKENS` | Max tokens cho response | 4000 |

## 📦 Các loại quan hệ văn bản

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

## 🐛 Troubleshooting

### Lỗi API Key
```
ValueError: API_KEY không được để trống
```
→ Kiểm tra file `.env` và đảm bảo đã set `OPENAI_API_KEY`

### Lỗi parse JSON
```
Không thể parse JSON từ response
```
→ Kiểm tra response từ LLM, có thể cần điều chỉnh prompt hoặc temperature

### Permission denied khi chạy scripts
```bash
chmod +x start_api.sh run.sh test_api.sh setup.sh
```

### Port 8000 đã được sử dụng
```bash
# Tìm process đang sử dụng port
lsof -i :8000

# Stop API
docker-compose down

# Hoặc đổi port trong docker-compose.yml
ports:
  - "8001:8000"
```

## 🚀 Deploy to Production

### Với Docker

```bash
# Build production image
docker build -t van-ban-analyzer:latest .

# Run container
docker run -d \
  -p 8000:8000 \
  --env-file .env \
  --name van-ban-analyzer \
  van-ban-analyzer:latest
```

### Với Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Environment Variables for Production

```bash
OPENAI_API_KEY=your-production-key
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=Qwen/Qwen3-8B
TEMPERATURE=0.1
MAX_TOKENS=4000
```

## 📊 Monitoring

### Check API Health
```bash
curl http://localhost:8000/health
```

### View Docker Logs
```bash
docker-compose logs -f
```

### API Metrics
Visit `http://localhost:8000/docs` for built-in API metrics and testing interface.

