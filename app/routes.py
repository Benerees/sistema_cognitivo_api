from fastapi import APIRouter, Query
from typing import Optional
from pydantic import BaseModel
from app.database import db
from datetime import datetime

router = APIRouter()

class EventLog(BaseModel):
    _id: str
    classe: str
    nome_item: str
    codigo: str
    data_hora: datetime
    total: float

@router.get("/event_logs", response_model=list[EventLog])
def get_event_logs(
    classe: Optional[str] = None,
    nome_item: Optional[str] = None,
    codigo: Optional[str] = None,
    total: Optional[float] = None,
    data_inicial: Optional[datetime] = Query(None, description="Formato: YYYY-MM-DDTHH:MM:SS"),
    data_final: Optional[datetime] = Query(None, description="Formato: YYYY-MM-DDTHH:MM:SS"),
):
    query_filter = {}

    if classe:
        query_filter["classe"] = classe
    if nome_item:
        query_filter["nome_item"] = nome_item
    if codigo:
        query_filter["codigo"] = codigo
    if total is not None:
        query_filter["total"] = total

    if data_inicial or data_final:
        query_filter["data_hora"] = {}
        if data_inicial:
            query_filter["data_hora"]["$gte"] = data_inicial
        if data_final:
            query_filter["data_hora"]["$lte"] = data_final

    event_logs = list(db.event_logs.find(query_filter).limit(100))

    for log in event_logs:
        log["_id"] = str(log["_id"])
        if isinstance(log.get("data_hora"), datetime):
            log["data_hora"] = log["data_hora"].isoformat()

    return event_logs
