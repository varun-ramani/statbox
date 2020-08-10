from enum import Enum

class CountType(Enum):
    EMAIL_ADDRESS = 1
    TLD = 2
    HOSTNAME = 3
    DOMAIN = 4

def count(messages, count_type):
    counts = {

    }

    for message in messages:
        email_address = message['From']['Email']

        if email_address == None:
            key = None

        else:
            if count_type == CountType.EMAIL_ADDRESS: key = email_address
            elif count_type == CountType.TLD: key = email_address.split('.')[-1]
            elif count_type == CountType.HOSTNAME: key = email_address.split('@')[-1]
            elif count_type == CountType.DOMAIN: key = ".".join(email_address.split('@')[-1].split('.')[-2:])
        
        if key not in counts:
            counts[key] = 0
        
        counts[key] += 1
    

    counts = {item[0]: item[1] for item in sorted(counts.items(), key=lambda x: x[1], reverse=True)}
    return counts