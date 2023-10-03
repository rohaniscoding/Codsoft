import random

# Define predefined rules and responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "help": "I can assist you with basic information. Just ask me a question!",
    "default": "I'm sorry, I don't understand. Please try again.",
}

# Function to generate a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    # Check for specific user queries
    if user_input in responses:
        return responses[user_input]
    elif "thank you" in user_input:
        return "You're welcome!"
    elif "weather" in user_input:
        return "I'm not equipped to provide weather information at the moment."
    else:
        return responses["default"]

# Main loop for chatting with the user
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
