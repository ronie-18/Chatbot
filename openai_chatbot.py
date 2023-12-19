from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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",
)

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
        
        