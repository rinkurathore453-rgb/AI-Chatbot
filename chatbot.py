print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Welcome!")

    elif user == "how are you":
        print("Bot: I am doing great!")

    elif user == "what is your name":
        print("Bot: I am a Rule-Based Chatbot.")

    elif user == "help":
        print("Bot: Ask me simple questions.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")