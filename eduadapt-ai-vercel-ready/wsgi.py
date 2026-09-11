"""
Entry point used to run the app with a production server (gunicorn/uvicorn).

Usage:
    uvicorn wsgi:app --host 0.0.0.0 --port 8000
    # or, with multiple worker processes:
    gunicorn wsgi:app -k uvicorn.workers.UvicornWorker -w 2 -b 0.0.0.0:8000
"""
from scripts.run_platform import EduAdaptPlatform
from api.endpoints import EduAdaptAPI

platform = EduAdaptPlatform()
app = EduAdaptAPI(platform).app
