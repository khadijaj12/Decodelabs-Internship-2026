# Rule-Based AI Chatbot — Project 1
# Skills: control flow, dictionary lookups, sanitization, continuous loop

# 1. KNOWLEDGE BASE — dictionary instead of if-elif ladder (O(1) lookup)
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great!",
    "what is your name": "I'm RuleBot, your friendly rule-based assistant.",
    "help": "You can ask me about my name, how I am, or just say hello!",
    "bye": "Goodbye! Have a great day.",
    "exit": "Goodbye! Have a great day.",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}

def get_response(user_input: str) -> str:
    """Look up a cleaned response, falling back to a default."""
    return responses.get(user_input, "I do not understand that yet. Try 'help'.")

def run_chatbot():
    print("RuleBot: Hello! Type 'bye' or 'exit' to end our chat.\n")

    while True:  # 2. INPUT LOOP — continuous 'while' cycle
        raw_input = input("You: ")

        # 3. SANITIZATION — handle case & whitespace
        clean_input = raw_input.lower().strip()

        if clean_input in EXIT_COMMANDS:  # 4. EXIT STRATEGY
            print("RuleBot: Goodbye! Have a great day.")
            break

        reply = get_response(clean_input)  # 5. FALLBACK built into .get()
        print(f"RuleBot: {reply}")

if __name__ == "__main__":
    run_chatbot()