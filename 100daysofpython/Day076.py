'''
Day 76: Chatbot
Create a chatbot using NLP libraries.
'''
from openai import OpenAI

client = OpenAI(api_key="", base_url="https://api.deepseek.com")



response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hello"},
],
stream=False
)
print(response.choices[0].message.content)

if __name__ == "__main__":
    while True:
        user_input = input("You:")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        reponse = chat_with_gpt(user_input)
        print("Chatbot: ", reponse)
