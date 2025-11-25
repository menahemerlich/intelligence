from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Reports(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    agent_id: int = Field(default=None, foreign_key="agents.id")
    terrorist_id: int = Field(default=None, foreign_key="terrorists.id")
    report: str
    date: datetime = datetime.now()