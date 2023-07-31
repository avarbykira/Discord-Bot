import openai

openai.api_key = "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"


def get_prompt(message):
    prompt = message[3:]
    return prompt


def get_completion(prompt):

    rules = "Reply with short and brief answer. "

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
