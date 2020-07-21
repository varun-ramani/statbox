import imaplib, ssl
import os, json
import time

from parser import parse_email
from insight import email_counts

from utils import print_histogram
import server_comm

import pickle

credentials = {}

if os.path.exists('creds.json'):
    with open('creds.json', 'r') as file:
        credentials = json.loads(file.read())

else:
    with open('creds.json', 'w+') as file:
        credentials = {
            "username": input("Enter email address: "),
            "password": input("Enter password: ")
        }
        file.write(json.dumps(credentials))

port = 993
email_address: str = credentials['username']
password: str = credentials['password']

username = email_address.split('@')[0]
server_hostname = 'imap.' + email_address.split('@')[1]

print()

server_comm.init(server_hostname=server_hostname, username=username, password=password, port=port)

messages = None
if os.path.exists('messagedump'):
    with open('messagedump', 'rb') as file:
        messages = pickle.load(file)
else:
    messages = server_comm.fetch_messages()
    with open('messagedump', 'wb+') as file:
        pickle.dump(messages, file)

print_histogram(email_counts(messages))