import imaplib, ssl
import os, json
import time

from parser import parse_email
from insight import count, CountType

from visual import bar_chart
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

server = server_comm.get_server(server_hostname=server_hostname, username=username, password=password, port=port)

fetcher = server_comm.ServerComm(server, verbose=True)

if os.path.exists('messagedump'):
    with open('messagedump', 'rb') as file:
        messages = pickle.load(file)
else:
    with open('messagedump', 'wb+') as file:
        fetcher.fetch_all()
        pickle.dump(fetcher.messages, file)
        messages = fetcher.messages

fetcher.delete_message('12')

with open('counts/email_address_counts.txt', 'w+') as file:
    file.write(bar_chart(count(messages, CountType.EMAIL_ADDRESS)))

with open('counts/tld_counts.txt', 'w+') as file:
    file.write(bar_chart(count(messages, CountType.TLD)))

with open('counts/hostname_counts.txt', 'w+') as file:
    file.write(bar_chart(count(messages, CountType.HOSTNAME)))

with open('counts/domain_counts.txt', 'w+') as file:
    file.write(bar_chart(count(messages, CountType.DOMAIN)))