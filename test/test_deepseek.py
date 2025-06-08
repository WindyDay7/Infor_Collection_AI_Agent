from openai import OpenAI

client = OpenAI(
    base_url='https://api-inference.modelscope.cn/v1/',
    api_key='9ddf95d0-a6fb-4631-a507-3ac67c698e0c', # ModelScope Token
)

response = client.chat.completions.create(
    model='deepseek-ai/DeepSeek-V3-0324', # ModelScope Model-Id
    messages=[
        {
            'role': 'system',
            'content': 'You are a helpful assistant.'
        },
        {
            'role': 'user',
            'content': '你好, 你知道故宫吗'
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end='', flush=True)


from openai import OpenAI

client = OpenAI(
    base_url='https://api-inference.modelscope.cn/v1/',
    api_key='9ddf95d0-a6fb-4631-a507-3ac67c698e0c', # ModelScope Token
)

response = client.chat.completions.create(
    model='deepseek-ai/DeepSeek-R1-0528', # ModelScope Model-Id
    messages=[
        {
            'role': 'user',
            'content': '你好'
        }
    ],
    stream=True
)
done_reasoning = False
for chunk in response:
    reasoning_chunk = chunk.choices[0].delta.reasoning_content
    answer_chunk = chunk.choices[0].delta.content
    if reasoning_chunk != '':
        print(reasoning_chunk, end='',flush=True)
    elif answer_chunk != '':
        if not done_reasoning:
            print('\n\n === Final Answer ===\n')
            done_reasoning = True
        print(answer_chunk, end='',flush=True)


from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-chat-v3-0324:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)


from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="<OPENROUTER_API_KEY>",
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