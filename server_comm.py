import imaplib
import time
from parser import parse_email
import ssl
import threading

server = None
context = None

def init(server_hostname, port, username, password):
    global server
    global context

    context = ssl.create_default_context()
    print(f"Connecting to '{server_hostname}':{port}")
    server = imaplib.IMAP4_SSL(server_hostname, port, ssl_context=context)
    try:
        print(f"Attempting login to '{server_hostname}'")
        server.login(username, password)
        print("Login successful!")

    except:
        print("Login failed.")
        exit()

class MailFetchThread(threading.Thread):
    def __init__(self, range, on_fetch, on_finish):
        self.range = range
        self.messages = []
        self.on_fetch = on_fetch
        self.on_finish = on_finish

    def run(self):
        for index in self.range:
            try:
                status, message = server.fetch(str(index).encode('utf-8'), '(RFC822)')
                self.messages.append(message)
                self.on_fetch(index, message)
            except:
                print(f"Failed to fetch message #{index}")

        self.on_finish(self.messages)

class MailFetcher():
    def __init__(self, server, context):
        

def fetch_messages():
    global server
    global context

    server.select("inbox")
    status, indices = server.search(None, 'ALL')

    if status != "OK":
        print("Failed to perform initial search. Abort.")
        exit()

    indices = indices[0].split()
    print(f"Found {len(indices)} emails.")
    print("Fetched {:4}/{:4} emails".format(0, len(indices)), end="\r")

    prev_time = time.time()
    times = [0.1] * (int(len(indices) / 20) + 1)

    messages = []

    for index in range(0, len(indices)):
        try:
            status, message = server.fetch(indices[index], '(RFC822)')
        except:
            print(f"Failed to fetch message #{int(indices[index])}\n\n")

        current_time = time.time()
        elapsed_time = current_time - prev_time
        times.pop(0)
        times.append(elapsed_time)
        avg_time = sum(times) / len(times)
        prev_time = current_time

        emails_remaining = len(indices) - index

        seconds_remaining = emails_remaining * avg_time
        seconds_remaining_str = ""

        if seconds_remaining < 60:
            seconds_remaining_str = "{:.1f} seconds remaining".format(seconds_remaining)

        elif seconds_remaining < 3600:
            seconds_remaining_str = "{:.1f} minutes remaining".format(seconds_remaining / 60)

        else:
            seconds_remaining_str = "{:.1f} hours remaining".format(seconds_remaining / 3600)

        print("Fetched {:4}/{:4} emails. {:20}.".format(index, len(indices), seconds_remaining_str), end="\r")

        try:
            messages.append(parse_email(message[0][1].decode('utf-8')))
        except:
            print(f"Can't decode message #{int(indices[index])}\n\n")

    return messages
