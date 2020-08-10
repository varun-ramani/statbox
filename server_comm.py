import imaplib
import time
from parser import parse_email
import ssl
import threading
import math
from utils import generate_batches

def get_server(server_hostname, port, username, password):
    context = ssl.create_default_context()
    server = imaplib.IMAP4_SSL(server_hostname, port, ssl_context=context)
    try:
        server.login(username, password)
        server.select("INBOX")
        return server
    except:
        print("Connection failed.")
        exit()

class ServerComm:
    def __init__(self, server, verbose=False):
        self.server: imaplib.IMAP4_SSL = server
        self.verbose = verbose

        self.total_messages = 0
        self.messages = []
        self.messages_downloaded = 0

        self.threads = []

    def thread_finished_callback(self, messages):
        self.messages += messages

    def thread_fetched_callback(self):
        self.messages_downloaded += 1
        if self.verbose:
            print("Fetched {:4}/{:4} emails.".format(self.messages_downloaded, self.total_messages, end="\r"))

    def fetch_all(self):
        self.server.select('inbox')
        status, indices = self.server.search(None, 'ALL')

        if status != 'OK':
            print("Failed to perform initial search. Abort.")
            exit()

        indices = indices[0].split()
        if self.verbose:
            print(f"Found {len(indices)} emails.")

        self.total_messages = len(indices)

        batches = generate_batches(1, len(indices) - 1, 50)

        for batch in batches:
            print(f'Downloading emails {batch[0]} through {batch[1]}')
            status, response = self.server.fetch(f'{batch[0]}:{batch[1]}', '(RFC822)')
            for item in response:
                if len(item) == 2:
                    decoded = item[1].decode('ISO-8859-1')
                    self.messages.append(parse_email(decoded))

    def delete_message(self, uid):
        self.server.store("3203", '+X-GM-LABELS', '\\Trash')