def send_messages(messages, sent_messages):
    for message in messages:
        print(message)
        sent_messages.append(message)