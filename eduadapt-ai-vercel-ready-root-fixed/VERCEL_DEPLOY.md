# EduAdapt AI - Vercel deployment

This package is prepared for Vercel's Python/FastAPI runtime.

## Deploy from GitHub

1. Put the CONTENTS of this folder at the root of a GitHub repository.
2. In Vercel, click **Add New -> Project** and import that repository.
3. Leave **Framework Preset** as Other / automatically detected.
4. Leave **Root Directory** as the repository root.
5. Do not add a custom Build Command or Start Command for the FastAPI function.
6. Click **Deploy**.

## Test after deployment

- `/` - deployment status
- `/api/health/` - API health check
- `/api/docs` - Swagger API documentation
- `/api/recommend-content/` - recommendations endpoint
- `/api/record-learning-session/` - session endpoint
- `/api/student-progress/{student_id}` - progress endpoint

## Local run

Install runtime dependencies:

    pip install -r requirements.txt

Then run:

    uvicorn api.index:app --reload

Open http://127.0.0.1:8000/api/docs

## Full ML/development dependencies

The original heavyweight ML/training dependencies are retained in
`requirements-full.txt`. They are intentionally not installed by Vercel's
runtime package because PyTorch/Plotly/Pandas are not required by the exposed
API execution paths and can make serverless deployments unnecessarily large.

For local training/development use:

    pip install -r requirements-full.txt
