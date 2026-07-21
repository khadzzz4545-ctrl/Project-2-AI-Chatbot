from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Store conversation history
history = []

print("=" * 50)
print("🤖 Gemini AI Chatbot (With Memory)")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    # Take user input
    user_input = input("\nYou: ")

    # Exit chatbot
    if user_input.lower() == "exit":
        print("\nGoodbye! 👋")
        break

    # Save user's message
    history.append(f"User: {user_input}")

    # Convert history list into one conversation
    conversation = "\n".join(history)

    # Send entire conversation to Gemini
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=conversation
    )

    # Print Gemini's response
    print("\nGemini:")
    print(response.text)

    # Save Gemini's response
    history.append(f"Assistant: {response.text}")