import sys
def get_bot_response(user_input):
    """Returns a predefined reply based on the user's input."""
    # Convert input to lowercase and remove extra spaces for consistent matching
    clean_input = user_input.lower().strip()
    
    # Predefined rules using if-elif-else blocks
    if clean_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif clean_input in ["how are you?", "how are you", "how's it going?"]:
        return "I'm fine, thanks!"
    elif clean_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye!"
    elif clean_input in ["who is your author?","who is your author"]:
        return "Rishta Singh"
    else:
        return "I am a simple bot. I don't understand that yet!"

def start_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    
    # Continuous loop for user interaction
    while True:
        try:
            # Get input from user
            user_message = input("You: ")
            
            # Get response from the logic function
            bot_reply = get_bot_response(user_message)
            
            # Print bot response
            print(f"Chatbot: {bot_reply}")
            
            # Break the loop if the user wants to say goodbye
            if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
                break
                
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye!")
            sys.exit()

# Run the chatbot application
if __name__ == "__main__":
    start_chatbot()