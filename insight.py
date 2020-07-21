def email_counts(messages):
    counts = {

    }

    for message in messages:
        email = message['From']['Email']
        if email not in counts:
            counts[email] = 0
        counts[email] = counts[email] + 1

    counts = {item[0]: item[1] for item in sorted(counts.items(), key=lambda x: x[1], reverse=True)}

    return counts