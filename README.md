# Test Deployment Workflow

This repository demonstrates a GitHub Actions workflow for deploying a web application with separate data and frontend components to GitHub Pages using Git worktrees.

## Features

- Separate workflows for data updates and frontend deployments
- Git worktree-based deployment system that eliminates merge conflicts
- Content preservation between different workflow runs
- Clean deployment branch strategy

## Structure

- `.github/workflows/`: GitHub Actions workflow files
- `scripts/`: Data generation scripts
- `data/`: Generated data files
- `frontend/`: SvelteKit frontend application

## Local Development

### Quick Setup

Use the provided setup script to initialize the local development environment:

```bash
# Make the script executable if needed
chmod +x setup-local-dev.sh

# Run the setup script
./setup-local-dev.sh
```

This will:
1. Generate sample data files
2. Create the necessary static directories for the frontend
3. Copy the data files to the frontend's static directory

### Running Data Generation Locally

To generate sample data manually:

```bash
# Make sure you have Python 3.12+ installed
python --version

# Run the data generation script
python scripts/generate_data.py

# Verify data was created
cat data/stats.json
```

### Running Frontend Locally

To run the SvelteKit frontend locally:

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# The development server will start at http://localhost:5173
```

You'll need to create a static link to the data directory for local development:

```bash
# From the frontend directory
mkdir -p static/data
cp ../data/stats.json static/data/
```

To build the frontend for production:

```bash
# From the frontend directory
npm run build

# Preview the production build
npm run preview
```

## Deployment Workflows

### Data Generation Workflow

The data generation workflow (`generate-data.yml`):
- Triggers on:
  - Push to main (data or scripts changes)
  - Manual workflow dispatch
  - Schedule (every 6 hours)
- Generates sample data
- Updates only the data files in the `github-pages-deployment` branch using git worktree
- Triggers the frontend deployment workflow when run via schedule or manual dispatch

### Frontend Deployment Workflow

The frontend deployment workflow (`deploy-frontend.yml`):
- Triggers on:
  - Push to main (frontend changes)
  - Manual workflow dispatch
- Builds the SvelteKit application
- Updates the frontend files in the `github-pages-deployment` branch using git worktree
- Preserves existing data files during deployment

## GitHub Pages Setup

For this workflow to work correctly with GitHub Pages:

1. Go to your repository settings
2. Navigate to Pages
3. Under "Build and deployment":
   - Select "Deploy from a branch"
   - Select the `github-pages-deployment` branch

## Testing the Workflow

1. Push this repository to GitHub
2. Run the "Generate Data" workflow manually from the Actions tab
3. The workflow will generate data and update the deployment branch
4. Run the "Deploy Frontend" workflow to build and update the frontend files
5. Visit the GitHub Pages URL to verify the site loads correctly with both frontend and data