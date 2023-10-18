import openai
import json
import os

openai.api_key = "API_KEY"

def call_ai(user, server):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": server
            },
            {
                "role": "user",
                "content": user
            }
        ],
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    res = response["choices"][0]["message"]["content"] # type: ignore
    return res
