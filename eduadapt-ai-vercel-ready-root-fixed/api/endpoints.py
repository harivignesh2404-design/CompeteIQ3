from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
from datetime import datetime, timezone
from typing import Dict, List, Any

class EduAdaptAPI:
    def __init__(self, learning_platform):
        self.app = FastAPI(title="EduAdapt AI API",
                          description="Personalized Learning Platform",
                          version="1.0.0")
        self.platform = learning_platform
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.get("/")
        async def root():
            return {
                "message": "EduAdapt AI API is running",
                "status": "online",
                "docs": "/docs",
                "health": "/health/"
            }

        @self.app.post("/recommend-content/")
        async def recommend_content(request: Dict[str, Any]):
            try:
                student_id = request.get('student_id')
                if not student_id:
                    raise HTTPException(status_code=400, detail='student_id is required')
                target_concepts = request.get('target_concepts', [])
                max_recommendations = request.get('max_recommendations', 5)
                
                recommendations = self.platform.get_personalized_recommendations(
                    student_id, target_concepts, max_recommendations
                )
                
                return JSONResponse(content=jsonable_encoder({
                    'student_id': student_id,
                    'recommendations': recommendations,
                    'timestamp': datetime.now(timezone.utc).isoformat()
                }))
            except HTTPException:
                raise
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/record-learning-session/")
        async def record_learning_session(request: Dict[str, Any]):
            try:
                student_id = request.get('student_id')
                if not student_id:
                    raise HTTPException(status_code=400, detail='student_id is required')
                session_data = request.get('session_data', {})
                
                self.platform.record_learning_session(student_id, session_data)
                
                return JSONResponse(content={
                    'status': 'success',
                    'message': 'Learning session recorded',
                    'student_id': student_id
                })
            except HTTPException:
                raise
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/student-progress/{student_id}")
        async def get_student_progress(student_id: str):
            try:
                progress = self.platform.get_student_progress(student_id)
                return JSONResponse(content=jsonable_encoder(progress))
            except HTTPException:
                raise
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/health/")
        async def health_check():
            return {"status": "healthy", "service": "EduAdapt AI"}
    
    def run(self, host: str = "0.0.0.0", port: int = 8000):
        uvicorn.run(self.app, host=host, port=port)