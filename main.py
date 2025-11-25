from fastapi import FastAPI, Depends
from sqlalchemy.dialects.mysql import insert
from sqlmodel import Session, select
from db import create_db_and_tables, get_session
from models.agents import Agents
from models.terrorists import Terrorists
from models.reports import Reports
from pydantic import BaseModel

app = FastAPI()
create_db_and_tables()

@app.get("/login/{agent_code}")
def login(agent_code: int, session: Session = Depends(get_session)):
    agent = session.exec(select(Agents).where(Agents.agent_code == agent_code)).first()
    if agent:
        return "התחברת בהצלחה"
    else:
        return "סוכן לא קיים"

class AddAgent(BaseModel):
    name: str
    agent_code: int

@app.post("/add_agent")
def add_agent(agent: AddAgent, session: Session = Depends(get_session)):
    session.add(agent)
    session.commit()
    return agent




