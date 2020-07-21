def parse_email(email):
    components = {
        "From": {
            "Name": None,
            "Email": None
        },
        "To": {
            "Name": None,
            "Email": None
        },
        "Subject": None,
        "Date": None
    }

    for line in email.split('\n'):
        for key in ['Subject', 'Date']:
            if line.startswith(key) and components[key] == None:
                components[key] = line[line.find(': ') + 2:].replace('\r', '')

        if line.startswith('From') and components['From']['Name'] == None:
            if " <" in line and ">" in line:
                components['From']['Name'] = line[line.find(': ') + 2:line.find(' <')].replace('"', '').replace("'", "")
                components['From']['Email'] = line[line.find(" <") + 2:line.find(">")]

        if line.startswith('To') and components['To']['Name'] == None:
            if " <" in line and ">" in line:
                components['To']['Name'] = line[line.find(': ') + 2:line.find(' <')].replace('"', '').replace("'", "")
                components['To']['Email'] = line[line.find(" <") + 2:line.find(">")]

    return components