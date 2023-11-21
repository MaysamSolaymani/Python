import openai

openai.organization = "org-Pd75www91CqOGH1dCT4w2lyw"
openai.api_key = "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"
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Q: Who is Batman?",
    temperature=0,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n\n"]
)
#######################
print(response)
