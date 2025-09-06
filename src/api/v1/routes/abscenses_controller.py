import os

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.dependencies import get_db
from src.usecase.save_abscense_from_sheet import save_abscense_from_sheet

router = APIRouter()


@router.get("/extract")
async def extract_data(db: AsyncSession = Depends(get_db)):
    spreadsheet_id = os.getenv("ABSCENSES_SPREADSHEET_ID")
    range_name = "abscenses"
    result = await save_abscense_from_sheet(spreadsheet_id, range_name, db)
    return {"message": result["message"]}
