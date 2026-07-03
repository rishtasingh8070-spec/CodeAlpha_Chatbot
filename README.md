# CodeAlpha_Chatbot
A python based  Chatbot with Pre-defined Replies.
Simple Python Chatbot 🤖

A beginner-friendly command-line chatbot built using Python. The chatbot responds to user messages with predefined responses using "if-elif-else" conditions.

Features

- Interactive command-line conversation
- Recognizes basic greetings
- Responds to simple questions
- Exit commands to end the chat
- Handles invalid or unknown inputs
- Supports graceful exit using keyboard interruption ("Ctrl + C")

How the Chatbot Works

1. The chatbot starts and greets the user.
2. The user enters a message.
3. The program converts the input to lowercase and removes extra spaces.
4. The chatbot checks the message against predefined rules:
   - Greeting messages → Returns a greeting
   - Basic questions → Returns a response
   - Exit commands → Ends the chat
   - Unknown inputs → Displays a default message
5. The process repeats until the user exits.

Technologies Used

- Python 3
- "sys" module

Run the Python file:

python chatbot.py

Example Conversation

Chatbot: Hello! Type 'bye' to exit the chat.

You: hello
Chatbot: Hi!

You: how are you?
Chatbot: I'm fine, thanks!

You: what is AI?
Chatbot: I am a simple bot. I don't understand that yet!

You: bye
Chatbot: Goodbye!

Project Structure

simple-chatbot/
│
├── chatbot.py
└── README.md

Supported Inputs

Greetings

- hello
- hi
- hey
- hola

Questions

- how are you?
- how are you
- how's it going?

Exit Commands

- bye
- goodbye
- exit
- quit

Future Improvements

- Add more conversation topics
- Use dictionaries instead of long "if-elif" statements
- Add date and time responses
- Add AI/NLP functionality
- Create a GUI version using Tkinter
- Store conversation history

Error Handling
The chatbot handles:

- "KeyboardInterrupt" ("Ctrl + C")
- "EOFError"
- Unknown user inputs
