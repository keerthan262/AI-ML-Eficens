import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key="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");#OpenAI_Key)

def chatbot():
    print("Chatbot: Hello! Ask me anything. Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0 
        )
        
        print("Chatbot:", response.choices[0].message.content.strip())      

# Run the chatbot
chatbot()
