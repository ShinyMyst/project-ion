import openai
openai.api_key = "NONE"

prompt = "Generate a unique name for a new ice cream flavor."
model = "text-davinci-002" # Ada
completions = openai.Completion.create(
    engine=model,
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5,
)

message = completions.choices[0].text.strip()
print(message)