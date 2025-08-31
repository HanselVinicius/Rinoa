from google.oauth2 import service_account
from googleapiclient.discovery import build


def extract_google_sheet():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    SERVICE_ACCOUNT_FILE = "../credentials.json"
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )
    service = build("sheets", "v4", credentials=creds)

    SPREADSHEET_ID = "placeholder"
    RANGE_NAME = "placeholder"

    sheet = service.spreadsheets()
    sheet_values = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
    )
    result = sheet_values.execute()
    values = result.get("values", [])

    print(values)
