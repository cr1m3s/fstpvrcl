from fastapi import FastAPI
from server.routes import router as NoteRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": "Hello world!"
    }

app.include_router(NoteRouter, prefix="/note")
