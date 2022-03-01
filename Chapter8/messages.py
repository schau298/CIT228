#import message_activity
#from message_activity *
#from message_activity import send_messages
def show_messages(messages):
    print("Your messages:")
    for message in messages:
        print(message)
 
  

def send_messages(messages, sent_messages):
   print("\nSending messages:")
   while messages:
        text = messages.pop()
        print(text)
        sent_messages.append(text)

messages = ["How is it going?", "What up?"," Hello there"]

show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\n All mesages:")
print(messages)
print(sent_messages)