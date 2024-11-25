from chatbot_interface import ChatbotInterface

def main():
    chatbot = ChatbotInterface()
    print("Welcome to the Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.chat(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
