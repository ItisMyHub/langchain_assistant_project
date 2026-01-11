from fastapi import FastAPI
from pydantic import BaseModel

from assistant import Assistant


# ----------------------------
# App setup
# ----------------------------

app = FastAPI(
    title="Local AI Assistant API",
    description="A local AI assistant built with LangChain + Ollama",
    version="0.1.0",
)

assistant = Assistant()


# ----------------------------
# Request / response models
# ----------------------------

class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    reply: str


# ----------------------------
# Routes
# ----------------------------

@app.get("/")
def root():
    return{
        "message": "Local AI Assistant API is running",
        "docs": "/docs",
    } 



@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    answer = assistant.run(
        query=req.message,
        session_id=req.session_id
    )
    return {"reply": answer}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
