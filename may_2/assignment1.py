import openai
import os
from dotenv import load_dotenv

load_dotenv() 
OpenAI_Key = os.getenv("OPENAI_API_KEY")

# Set your API key
client = openai.OpenAI(api_key=OpenAI_Key)

prompt ={
    "Simple": "Summarize this news article.",
    "Detailed": "Provide a summary of the following news article, people involved, and outcomes.",
    "Tone Specific": "Summarize the news article in a neutral tone and key points",
}
def article(key, value):
    print("ArticleChatbot: Hello! Ask me about an article. Type 'exit' to quit.");

    while True:
        user_input = input("You : ")
        if user_input.lower() in ['exit', 'quit']:
            print("ArticleChatbot: Goodbye!")
            break
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content":value },
                {"role": "user", "content": user_input}
            ],
            temperature=0 
        )
        return response.choices[0].message.content.strip();

for key,value in prompt.items():
    res = article(key,value);
    print(f" {key} : {res}");

