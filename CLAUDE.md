# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains a GitHub Actions workflow solution for deploying a web application with separate data and frontend components. The system is designed to avoid merge conflicts by using clean branch management techniques.

## Key Concepts

- **Separate Concerns**: Data updates and frontend deployments are handled by different workflows
- **Branch Strategy**: Uses a clean `github-pages-deployment` branch with no connection to previous history
- **File Preservation**: Each workflow preserves files managed by the other workflow
- **Git Worktree**: Used to manage branch content updates without conflicting changes
- **Commit Attribution**: Never add Claude Code attribution to git commits

## Commands

### Python Setup

```bash
# Install dependencies
pip install -e .

# Run the data generation script
python scripts/generate_data.py
```

### Frontend Development (assuming SvelteKit)

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

## Workflow Files

The repository contains two main GitHub Actions workflows:

1. **Data Generation**: Generates data and updates only the data directory in the deployment branch
2. **Frontend Deployment**: Builds the frontend and updates only the frontend files in the deployment branch

## Repository Structure

- `.github/workflows/`: Contains the GitHub Actions workflow files
- `scripts/`: Contains data generation scripts
- `data/`: Contains generated data files
- `frontend/`: Contains the SvelteKit frontend application

## Implementation Details

- Data and frontend files are managed separately to avoid conflicts
- The `github-pages-deployment` branch contains only production-ready files
- Workflows use file preservation techniques to avoid overwriting each other's content
- Special care is taken to handle the first-time setup of the deployment branch

## Testing Workflows

Workflows can be manually triggered from the GitHub Actions tab to test the deployment process.