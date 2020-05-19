import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None

    if 'CREDS_HEX' in os.environ:
        creds = os.environ['CREDS_HEX']
        creds = bytearray.fromhex(creds)
        creds = pickle.loads(creds)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            config = json.loads(os.environ['CRED'])
            flow = InstalledAppFlow.from_client_config(
                config, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('.env', 'a', encoding='UTF-8') as f:
            f.write(f'\nCREDS_HEX={pickle.dumps(creds).hex()}\n')

    service = build('gmail', 'v1', credentials=creds)

    # pylint: disable=no-member
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    print(f'You have {len(labels)} labels')

if __name__ == '__main__':
    main()
