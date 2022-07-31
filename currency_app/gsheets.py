from __future__ import print_function

import os.path
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .models import Product

# if modifying these scopes, delete the file token.json
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

BASE_DIR = Path(__file__).resolve().parent.parent

# the ID and range of the spreadsheet
SAMPLE_SPREADSHEET_ID = '1pDCNye1y8u7GphQpR6tbQu-eK9zk9wdOsR951TddAgI'
SAMPLE_RANGE_NAME = 'A2:D'


def make_a_table():
    creds = None
    # the file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # if there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                BASE_DIR / 'currency_app/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        for row in values:
            # adding new products to the database
            if Product(id=row[0], order_number=row[0], price_usd=row[1], delivery_date=str(row[3].split('.')[::-1][0]) + '-' + str(row[3].split('.')[::-1][1]) + '-' + str(row[3].split('.')[::-1][2])) not in Product.objects.all():
                product = Product(id=row[0], order_number=row[1], price_usd=row[2],
                                  delivery_date=str(row[3].split('.')[::-1][0]) + '-' + str(
                                      row[3].split('.')[::-1][1]) + '-' + str(row[3].split('.')[::-1][2]))
                product.save()
    except HttpError as err:
        print(err)
