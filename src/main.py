import os
from extract_google_sheet import extract_google_sheet
from dotenv import load_dotenv

from db import Base,engine

def init_db():
    Base.metadata.create_all(bind=engine)

def main():
    load_dotenv()
    init_db()
    spreadsheet_id = os.getenv("ABSCENSES_SPREADSHEET_ID")
    range_name = "abscenses"
    extract_google_sheet(spreadsheet_id, range_name)

if __name__ == "__main__":
    main()
