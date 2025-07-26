from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, UploadFile, HTTPException
from app.controller.controller import add_text_into_db
from app.databases.fakedatabase import FakeDatabase
from app.agents.fakeagent import FakeAgent
from app.interfaces.database import DatabaseI


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = FakeDatabase()
    agent = FakeAgent()
    yield {"db": db, "agent": agent}


app = FastAPI(lifespan=lifespan)


@app.post("/add-document")
def add_document(request: Request, file: UploadFile):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=403, detail="format not allowed")
    db: DatabaseI = request.state.db
    add_text_into_db(db=db, text=file.file.read().decode())
