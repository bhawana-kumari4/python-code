
def get_reply(user_input):
    user_input = user_input.lower() 

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

print("Chatbot is running. Type 'bye' to exit.\n")

while True:
    user_message = input("You: ")
    reply = get_reply(user_message)
    print("Bot:", reply)

    if user_message.lower() == "bye":
        break

