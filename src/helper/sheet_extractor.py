from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
SERVICE_ACCOUNT_FILE = "credentials.json"

class SheetTypes:
    GOOGLE_SHEETS = "google_sheets"

class SheetExtractor:

    def __init__(self, spreadsheet_type):
        self.spreadsheet_type = spreadsheet_type

    def extract(self):
        if self.spreadsheet_type == SheetTypes.GOOGLE_SHEETS:
            return self.extract_google_sheet()
        else:
            raise ValueError("Unsupported spreadsheet type")

    def extract_google_sheet(self,spreadsheet_id, range):

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
