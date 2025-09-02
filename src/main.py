import os
from extract_google_sheet import extract_google_sheet
from dotenv import load_dotenv

def main():
    load_dotenv()
    spreadsheet_id = os.getenv("ABSCENSES_SPREADSHEET_ID")
    range_name = "abscenses"
    extract_google_sheet(spreadsheet_id, range_name)

if __name__ == "__main__":
    main()
