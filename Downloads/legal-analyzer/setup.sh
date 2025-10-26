#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}=== Van Ban Analyzer - Setup Script ===${NC}\n"

# Create directory structure
echo -e "${GREEN}Creating directory structure...${NC}"
mkdir -p van_ban_analyzer/{models,services,prompts,utils}
mkdir -p data output

# Create .gitkeep files
touch data/.gitkeep
touch output/.gitkeep

# Create __init__.py files
echo -e "${GREEN}Creating __init__.py files...${NC}"

# van_ban_analyzer/__init__.py
cat > legal_analyzer/__init__.py << 'EOF'
"""Van Ban Analyzer - Phân tích quan hệ văn bản pháp luật Việt Nam"""

__version__ = "1.0.0"

from legal_analyzer.services.analyzer import VanBanAnalyzer
from legal_analyzer.config import Config

__all__ = ['VanBanAnalyzer', 'Config']
EOF

# van_ban_analyzer/models/__init__.py
cat > legal_analyzer/templates/__init__.py << 'EOF'
"""Template cho văn bản pháp luật"""

from legal_analyzer.templates.van_ban import (
    VanBan,
    QuanHeVanBan,
    VanBanRelationResult
)

__all__ = ['VanBan', 'QuanHeVanBan', 'VanBanRelationResult']
EOF

# van_ban_analyzer/services/__init__.py
cat > legal_analyzer/services/__init__.py << 'EOF'
"""Services cho phân tích văn bản"""

from legal_analyzer.services.legal_doc_analyzer import VanBanAnalyzer

__all__ = ['VanBanAnalyzer']
EOF

# van_ban_analyzer/utils/__init__.py
cat > legal_analyzer/utils/__init__.py << 'EOF'
"""Utilities"""

from van_ban_analyzer.utils.uuid_generator import UUIDGenerator

__all__ = ['UUIDGenerator']
EOF

# van_ban_analyzer/prompts/__init__.py
cat > legal_analyzer/prompts/__init__.py << 'EOF'
"""Prompt builders"""

from van_ban_analyzer.prompts.prompt_builder import PromptBuilder

__all__ = ['PromptBuilder']
EOF

# Create .env from example if not exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}Creating .env file from template...${NC}"
    cp .env.example .env
    echo -e "${YELLOW}⚠️  Please update .env with your API credentials${NC}"
fi

# Make scripts executable
echo -e "${GREEN}Making scripts executable...${NC}"
chmod +x run.sh

echo -e "\n${GREEN}✅ Setup complete!${NC}\n"
echo -e "${BLUE}Next steps:${NC}"
echo "1. Update .env file with your API credentials"
echo "2. Place your JSON files in the 'data' directory"
echo "3. Run: ./run.sh local data/van_ban_a.json"
echo ""
echo -e "${BLUE}Or use Docker:${NC}"
echo "1. Update .env file with your API credentials"
echo "2. Run: ./run.sh docker data/van_ban_a.json"