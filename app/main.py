from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, UploadFile, HTTPException
from app.controller.controller import add_text_into_db, query_the_agent
from app.databases.fakedatabase import FakeDatabase
# from app.agents.fakeagent import FakeAgent
from app.agents.cohereagent import ChatCohere, CohereAgent
from app.interfaces.database import DatabaseI
from app.interfaces.agent import AIAgentI


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = FakeDatabase()
    agent = CohereAgent()
    yield {"db": db, "agent": agent}


app = FastAPI(lifespan=lifespan)


@app.post("/add-document")
def add_document(request: Request, file: UploadFile):
    if file.content_type != "text/plain":
        raise HTTPException(status_code=403, detail="format not allowed")
    db: DatabaseI = request.state.db
    add_text_into_db(db=db, text=file.file.read().decode())


@app.post("/query-agent")
def query_agent(request: Request, question: str):
    agent: AIAgentI = request.state.agent
    db: DatabaseI = request.state.db
    answer = query_the_agent(db=db, agent=agent, question=question)
    return answer
