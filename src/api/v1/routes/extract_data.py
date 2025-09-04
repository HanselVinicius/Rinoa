import os
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from extract_google_sheet import extract_google_sheet
from infra.dependencies import get_db
from model.abscenses import Abscenses

router = APIRouter()


@router.get("/extract")
async def extract_data(db: AsyncSession = Depends(get_db)):
    spreadsheet_id = os.getenv("ABSCENSES_SPREADSHEET_ID")
    range_name = "abscenses"
    returned_data = extract_google_sheet(spreadsheet_id, range_name)

    if not returned_data or len(returned_data) < 2:
        return {"message": "No data found in the sheet."}

    for row in returned_data[1:]:
        timestamp_str, name, reason, date_str = row[:4]

        absense_date = datetime.strptime(date_str, "%d/%m/%Y").date()

        abscense = Abscenses(name=name, absense_type=reason, absense_date=absense_date)
        db.add(abscense)

    await db.commit()

    return {"message": f"{len(returned_data) - 1} rows inserted."}
