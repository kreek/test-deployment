#!/usr/bin/env bash

# sync-data.sh - Script to synchronize data files between data/ and frontend/static/data/
# Also runs the data generation script if requested

set -e

# Define colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Define source and destination paths
SOURCE_DIR="data"
DEST_DIR="frontend/static/data"

# Check if we should generate new data first
if [ "$1" == "--generate" ] || [ "$1" == "-g" ]; then
  echo -e "${YELLOW}Generating fresh data...${NC}"
  python scripts/generate_data.py
  echo ""
fi

# Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: Source directory $SOURCE_DIR does not exist."
  exit 1
fi

# Create destination directory if it doesn't exist
mkdir -p "$DEST_DIR"

# Copy all files from source to destination
echo -e "${YELLOW}Syncing data files to frontend:${NC}"
for file in "$SOURCE_DIR"/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    cp -v "$file" "$DEST_DIR/$filename"
  fi
done

echo -e "\n${GREEN}Sync complete!${NC}"

# Show tip for development
echo -e "${YELLOW}Tip:${NC} If your SvelteKit dev server is running, refresh the page to see the updated data."