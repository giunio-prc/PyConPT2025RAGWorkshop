from app.interfaces.database import DatabaseI
from app.interfaces.agent import AIAgentI


def add_text_into_db(db: DatabaseI, text: str):
    db.add_text(text=text)


def query_the_agent(db: DatabaseI, agent: AIAgentI, question: str) -> str:
    context = db.get_context(question=question)
    answer = agent.query_agent(question=question, context=context)
    return answer
