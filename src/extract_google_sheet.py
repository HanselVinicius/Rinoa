from google.oauth2 import service_account
from googleapiclient.discovery import build


def extract_google_sheet(spreadsheet_id, range):
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    SERVICE_ACCOUNT_FILE = "../credentials.json"
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()
    sheet_values = sheet.values().get(
        spreadsheetId=spreadsheet_id,
        range=range,
    )
    result = sheet_values.execute()
    values = result.get("values", [])
    return values
