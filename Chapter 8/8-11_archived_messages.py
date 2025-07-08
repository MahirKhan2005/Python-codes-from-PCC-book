def send_messages(messages,sents):
    while messages:
        for message in messages:
            print(message)
            sents.append(messages.pop())
texts = ["I'm learing Python", 'I am also learning C', "Soon i'll be learning hacking" ]
sent_messages = []
send_messages(texts[:],sent_messages)
print(texts)
print(sent_messages)
