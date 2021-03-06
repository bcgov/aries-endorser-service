import logging
from typing import Optional
import json

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from api.endpoints.dependencies.db import get_db


logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/summary", status_code=status.HTTP_200_OK, response_model=dict)
async def get_transaction_report() -> dict:
    # this should take some query params, sorting and paging params...
    return {}


@router.get(
    "/summary/{connection_id}", status_code=status.HTTP_200_OK, response_model=dict
)
async def get_connection_transaction_report(
    connection_id: str,
) -> dict:
    # this should take some query params, sorting and paging params...
    return {}
