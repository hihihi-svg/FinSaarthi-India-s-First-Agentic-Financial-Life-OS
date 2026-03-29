from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional

from finsaarthi.agents.orchestrator import FinSaarthiOrchestrator
from finsaarthi.rag.knowledge_base import FinSaarthiKnowledgeBase

app = FastAPI(title="FinSaarthi API")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, specify the exact origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Knowledge Base and Orchestrator
# Note: For now, we use a mock KB if dependencies are still loading
try:
    kb = FinSaarthiKnowledgeBase()
except Exception as e:
    print(f"RAG Knowledge Base not ready: {e}. Using mock.")
    class MockKB:
        def query(self, q, k=2): return []
    kb = MockKB()

orchestrator = FinSaarthiOrchestrator(kb)

class QueryRequest(BaseModel):
    user_input: str
    user_profile: Dict

@app.get("/")
async def root():
    return {"message": "FinSaarthi API is running"}

@app.post("/query")
async def process_query(request: QueryRequest):
    try:
        result = orchestrator.run(request.user_input, request.user_profile)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
