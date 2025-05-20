#!/bin/bash

# Generate sample data
echo "Generating sample data..."
python scripts/generate_data.py

# Create static directory for frontend
echo "Setting up static data directory for frontend..."
mkdir -p frontend/static/data
cp data/stats.json frontend/static/data/

echo "Local development environment setup complete!"
echo ""
echo "To run the frontend:"
echo "  cd frontend"
echo "  npm install"
echo "  npm run dev"
echo ""
echo "The site will be available at http://localhost:5173"