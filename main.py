# main.py
from google import genai
from config import API_KEY

def get_response(prompt):
    # Initialize the genai client with your API key
    client = genai.Client(api_key=API_KEY)
    
    # Send the user's prompt to the Gemini 2.0 Flash model
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt]
    )
    
    # Return the text generated by the model
    return response.text

def run_cli():
    print("Welcome to the Gemini Flash2.0 Chatbot (CLI)!")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ["exit", "quit"]:
            print("Exiting chatbot. Goodbye!")
            break
        
        bot_response = get_response(user_input)
        print("Bot:", bot_response)

if __name__ == "__main__":
    run_cli()
