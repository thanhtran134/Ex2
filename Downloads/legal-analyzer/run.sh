#!/bin/bash

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}=== Van Ban Analyzer API ===${NC}\n"

# Check mode
MODE=${1:-docker}

if [ "$MODE" == "docker" ]; then
    echo -e "${GREEN}Starting API with Docker...${NC}\n"

    CONTAINER_NAME="van-ban-analyzer-api"

    # Check if container already exists
    if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
        echo -e "${YELLOW}🧹 Removing existing container '$CONTAINER_NAME'...${NC}"
        docker rm -f $CONTAINER_NAME >/dev/null 2>&1
    fi

    # Build and start
    docker compose up --build -d

    if [ $? -eq 0 ]; then
        echo -e "\n${GREEN}✅ API is running!${NC}"
        echo -e "${BLUE}API URL:${NC} http://localhost:8686"
        echo -e "${BLUE}Docs:${NC} http://localhost:8686/docs"
        echo -e "${BLUE}Health:${NC} http://localhost:8686/health"
        echo ""
        echo -e "${YELLOW}View logs:${NC} docker compose logs -f"
        echo -e "${YELLOW}Stop API:${NC} docker compose down"
    else
        echo -e "${RED}Failed to start API${NC}"
        exit 1
    fi

elif [ "$MODE" == "local" ]; then
    echo -e "${GREEN}Starting API locally...${NC}\n"
    
    # Check virtual environment
    if [ ! -d "venv" ]; then
        echo "Creating virtual environment..."
        python3 -m venv venv
    fi

    source venv/bin/activate

    echo "Installing dependencies..."
    pip install -r requirements.txt

    if [ $? -ne 0 ]; then
        echo -e "${RED}Failed to install dependencies${NC}"
        exit 1
    fi

    echo -e "\n${GREEN}Starting API server...${NC}\n"
    uvicorn api.server:app --host 0.0.0.0 --port 8686 --reload

else
    echo -e "${RED}Invalid mode. Use 'docker' or 'local'${NC}"
    echo "Usage: ./start_api.sh [docker|local]"
    exit 1
fi
