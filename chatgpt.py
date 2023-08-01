import openai
import json

# save token in a json file to access
with open('token.json', 'r') as json_file:
    token = json.load(json_file)

openai.api_key = token["openai_token"]


def get_prompt(message):
    prompt = message[3:]
    return prompt


def get_completion(prompt):

    rules = "Reply with a brief answer. "
    # rules = " "

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": rules+prompt}]
    )
    return completion


def get_output(prompt):
    completion = get_completion(prompt)
    reply = completion["choices"][0]["message"]["content"]
    token_used = completion["usage"]["total_tokens"]

    return [reply, token_used]
