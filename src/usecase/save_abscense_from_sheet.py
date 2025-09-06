from datetime import datetime
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.helper.sheet_extractor import SheetExtractor, SheetTypes
from src.infra.dependencies import get_db
from src.model.abscenses import Abscenses

async def save_abscense_from_sheet(spreadsheet_id, range_name, db: AsyncSession = Depends(get_db)):
    sheet_extractor = SheetExtractor(spreadsheet_type=SheetTypes.GOOGLE_SHEETS)
    returned_data = sheet_extractor.extract_google_sheet(spreadsheet_id, range_name)

    if not returned_data or len(returned_data) < 2:
        return {"message": "No data found in the sheet."}

    for row in returned_data[1:]:
        timestamp_str, name, reason, date_str = row[:4]
        absense_date = datetime.strptime(date_str, "%d/%m/%Y").date()

        abscense = Abscenses(name=name, absense_type=reason, absense_date=absense_date,timestamp=datetime.strptime(timestamp_str, "%d/%m/%Y %H:%M:%S"))
        db.add(abscense)

    await db.commit()

    return {"message": f"{len(returned_data) - 1} rows inserted."}
