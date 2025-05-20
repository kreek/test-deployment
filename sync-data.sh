#!/usr/bin/env bash

# Define source and destination paths
SOURCE_FILE="data/stats.json"
DEST_DIR="frontend/static/data"
DEST_FILE="$DEST_DIR/stats.json"

# Check if source file exists
if [ ! -f "$SOURCE_FILE" ]; then
  echo "Error: Source file $SOURCE_FILE does not exist."
  exit 1
fi

# Check if destination directory exists, create if not
if [ ! -d "$DEST_DIR" ]; then
  mkdir -p "$DEST_DIR"
  echo "Created directory: $DEST_DIR"
fi

# Copy the file
cp "$SOURCE_FILE" "$DEST_FILE"

# Check if copy was successful
if [ $? -eq 0 ]; then
  echo "Successfully copied $SOURCE_FILE to $DEST_FILE"
else
  echo "Error: Failed to copy file."
  exit 1
fi