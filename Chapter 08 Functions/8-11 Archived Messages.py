def send_messages(print_messages, sent_messages):
    while print_messages:
        current_message = print_messages.pop()
        print(f"Current message: {current_message}")
        sent_messages.append(current_message)


msgs = ['hello', 'hi', 'sup']
sent_msgs = []

send_messages(msgs[:], sent_msgs)

print(msgs)
print(sent_msgs)

############################################################################
# Answer:

# def show_messages(messages):
#     """Print all messages in the list."""
#     print("Showing all messages:")
#     for message in messages:
#         print(message)


# def send_messages(messages, sent_messages):
#     """Print each message, and then move it to sent_messages."""
#     print("\nSending all messages:")
#     while messages:
#         current_message = messages.pop()
#         print(current_message)
#         sent_messages.append(current_message)


# messages = ["hello there", "how are u?", ":)"]
# show_messages(messages)

# sent_messages = []
# send_messages(messages[:], sent_messages)

# print("\nFinal lists:")
# print(messages)
# print(sent_messages)
