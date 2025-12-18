#!/bin/bash

# Script to record Asciinema demos
# Usage: ./scripts/record-demo.sh <demo-name>

if [ -z "$1" ]; then
    echo "Usage: $0 <demo-name>"
    echo "Example: $0 setup"
    exit 1
fi

DEMO_NAME="$1"
OUTPUT_FILE="docs/tutorials/${DEMO_NAME}.cast"

echo "Recording Asciinema demo: $DEMO_NAME"
echo "Output: $OUTPUT_FILE"
echo ""
echo "Press Ctrl+D when finished recording"
echo ""

asciinema rec "$OUTPUT_FILE"

echo ""
echo "Demo recorded to $OUTPUT_FILE"
echo "View with: asciinema play $OUTPUT_FILE"
