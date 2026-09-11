"""Vercel ASGI entry point for EduAdapt AI.

Vercel routes Python requests under /api/* to this module.  The existing
application keeps its original route paths (for example /health/), so it is
mounted under /api here.  This preserves local compatibility while exposing:

    /api/health/
    /api/recommend-content/
    /api/record-learning-session/
    /api/student-progress/{student_id}
    /api/docs
"""
from fastapi import FastAPI
from wsgi import app as eduadapt_app

app = FastAPI(title="EduAdapt AI - Vercel Gateway")
app.mount("/api", eduadapt_app)

@app.get("/")
async def root():
    return {
        "service": "EduAdapt AI",
        "status": "running",
        "api_base": "/api",
        "docs": "/api/docs",
        "health": "/api/health/",
    }
