from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-r1-0528:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)