# Test Deployment Workflow

This repository demonstrates a GitHub Actions workflow for deploying a web application with separate data and frontend components, avoiding merge conflicts using a clean branch strategy.

## Features

- Separate workflows for data updates and frontend deployments
- Clean `github-pages-deployment` branch with no connection to previous history
- File preservation between different workflow runs
- Git worktree for efficient branch content updates

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

## Usage in GitHub Actions

### Data Generation

The data generation workflow:
- Runs on schedule or manual trigger
- Generates sample data
- Updates only the data directory in the deployment branch
- Preserves frontend files

### Frontend Deployment

The frontend deployment workflow:
- Runs on push to main or when triggered by the data workflow
- Builds the SvelteKit application
- Updates only the frontend files in the deployment branch
- Preserves data files

## GitHub Pages Setup

For this to work correctly with GitHub Pages:
1. Go to your repository settings
2. Navigate to Pages
3. Set the source to the `github-pages-deployment` branch

## Testing the Workflow

1. Push this repository to GitHub
2. Run the "Generate Data" workflow manually from the Actions tab
3. The workflows will set up the deployment branch and deploy the site
4. Visit the GitHub Pages URL to verify the site loads correctly