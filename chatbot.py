# chatbot.py
# Rule-Based AI Chatbot


responses = {
    # Greetings
    "hello": "Hello! Welcome to RuleBot.",
    "hi": "Hi there! Nice to chat with you.",
    "hii": "Hi there! Nice to chat with you.",
    "hey": "Hey! How can I help?",
    "good morning": "Good morning! Have a productive day.",
    "good afternoon": "Good afternoon! Hope the day is going well.",
    "good evening": "Good evening! Nice to chat.",

    # General questions
    "how are you": "I am doing well. Thank you for asking.",
    "what is your name": "My name is RuleBot.",
    "what can you do": "I can answer greetings and general questions using rule-based logic.",
    "can you help me": "Yes, I can help with greetings and general questions.",
    "how can you help me": "I can respond to greetings, general questions, polite messages, and exit commands.",
    "what are you doing": "I am responding to your messages.",
    "are you busy": "No, I am available to chat.",
    "do you understand me": "I can understand predefined questions and respond using rules.",

    # Polite messages
    "thank you": "You're welcome.",
    "thanks": "You're welcome.",
    "nice to meet you": "Nice to meet you too.",
    "sorry": "No problem.",
    "ok": "Alright.",
    "okay": "Alright.",

    # Help and exit
    "help": "I can answer only greetings and general questions. Try: hello, hi, good morning, how are you, what is your name, what can you do, thank you, or bye.",
    "bye": "Goodbye! Have a nice day.",
    "exit": "Chat ended. See you again."
}


def clean_input(user_input):
    clean_text = user_input.lower().strip()
    clean_text = " ".join(clean_text.split())
    return clean_text


def get_response(user_input):
    clean_text = clean_input(user_input)

    if clean_text == "":
        return "Please type something.", False

    if clean_text == "bye" or clean_text == "exit":
        return responses[clean_text], True

    reply = responses.get(
        clean_text,
        "Sorry, I don't understand that. Type 'help' to see what I can answer."
    )

    return reply, False


def start_chatbot():
    print("Bot: Hello! I am RuleBot.")
    print("Bot: Type 'help' to see available questions.")
    print("Bot: Type 'bye' or 'exit' to stop the chat.")

    while True:
        user_message = input("You: ")

        reply, end_chat = get_response(user_message)

        print("Bot:", reply)

        if end_chat:
            break


if __name__ == "__main__":
    start_chatbot()