# Task 8: Rule-Based Chatbot using if-elif-else

print("Hello! I'm ChatBot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you today?")
    
    elif "your name" in user_input:
        print("Bot: I'm a simple chatbot created using Python!")
    
    elif "how are you" in user_input:
        print("Bot: I'm good, thank you! How about you?")
    
    elif "fine" in user_input or "good" in user_input:
        print("Bot: That's great to hear!")
    
    elif "help" in user_input:
        print("Bot: Sure! I can answer simple questions. Try asking me about the weather, your name, or say hi.")
    
    elif "weather" in user_input:
        print("Bot: I can't check live weather, but it’s always sunny in here!")
    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    
    else:
        print("Bot: I'm not sure how to respond to that. Can you try something else?")
