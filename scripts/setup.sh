#!/bin/bash
set -e

echo "Setting up Ambient Code Reference Repository..."

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Install dependencies
echo "Installing dependencies..."
uv pip install -r requirements-dev.txt

# Verify installation
echo "Verifying installation..."
python -c "from app.main import app; print('✓ Application imports successfully')"
pytest --collect-only > /dev/null && echo "✓ Tests discovered successfully"

echo ""
echo "Setup complete! 🎉"
echo ""
echo "Next steps:"
echo "  1. Activate virtual environment: source .venv/bin/activate"
echo "  2. Start the application: uvicorn app.main:app --reload"
echo "  3. Visit: http://localhost:8000/docs"
echo ""
