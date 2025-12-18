#!/bin/bash
set -e

echo "Validating Mermaid diagrams..."

# Find all .mmd files
MMD_FILES=$(find docs -name "*.mmd" 2>/dev/null || true)

if [ -z "$MMD_FILES" ]; then
    echo "No .mmd files found. Skipping Mermaid validation."
    exit 0
fi

# Check if mmdc is installed
if ! command -v mmdc &> /dev/null; then
    echo "Error: mermaid-cli (mmdc) is not installed"
    echo "Install with: npm install -g @mermaid-js/mermaid-cli"
    exit 1
fi

# Validate each diagram
ERRORS=0
for file in $MMD_FILES; do
    echo "Validating $file..."
    if ! mmdc -i "$file" -o /dev/null 2>&1; then
        echo "✗ Error in $file"
        ERRORS=$((ERRORS + 1))
    else
        echo "✓ $file is valid"
    fi
done

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "Found $ERRORS invalid Mermaid diagram(s)"
    exit 1
fi

echo ""
echo "All Mermaid diagrams are valid! ✓"
