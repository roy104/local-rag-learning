import ollama

messages = []
system_message = 'You are a helpful and curious AI assistant.'

# Define a function to create new messages with
# specified roles ('user' or 'assistant')
def create_message(message, role):
    return {
        'role': role,
        'content': message
    }

# Start the main conversation loop
def chat():
    # Call the ollama API to get the assistant response
    response = ollama.chat(model='llama3.2', stream=True, messages=messages)
    # Prepare the assistant message by concatenating all received chunks from the API
    assistant_message = ''
    for chunk in response:
        assistant_message += chunk['message']['content']
        print(chunk['message']['content'], end='', flush=True)
    # Add the finalized assistant message to the chat log
    messages.append(create_message(assistant_message, 'assistant'))

# Function for asking questions - append user messages to the chat logs before starting the `chat()` function
def ask(message):
    messages.append(
        create_message(message, 'user')
    )
    chat()

# Main interactive loop
def interactive_chat():
    print("You can start chatting with the AI assistant. Type 'exit' to end the chat.")
    while True:
        user_input = input("\n\nYou: ")
        if user_input.lower() == 'exit':
            print("Ending the chat. Goodbye!")
            break
        ask(user_input)

# Start the interactive chat
interactive_chat()