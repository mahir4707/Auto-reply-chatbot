from openai import OpenAI
client = OpenAI()(
    api_key="OPEN_AI_KEY"
)

command = '''

'''
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a person named mahir who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and talk like Mahir. output should be (message only)."
        },
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message.content)

