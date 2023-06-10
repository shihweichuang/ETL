import requests
import pprint

api_secret_key = "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"

headers = {
    "Authorization": f"Bearer {api_secret_key}",
    "OpenAI-Organization": "org-wwZDGXkmBszPlf2tZlZw3IkS"
}

api_url = "https://api.openai.com/v1/models"

res = requests.get(api_url, headers=headers)

# pprint.pprint(res.json()) # 回傳大量json資料

while True:
  prompt = input(">>")
  prompt_data = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 7,
    # "temperature": 0,
    # "top_p": 1,
    # "n": 1,
    # "stream": False,
    # "logprobs": None,
    # "stop": "\n"
  }

  prompt_url = "https://api.openai.com/v1/completions"  # 宣告一新變數url
  res = requests.post(prompt_url, headers=headers, json=prompt_data)
  ans = res.json()["choices"][0]["text"]
  # pprint.pprint(res.json())
  print("Output:", ans)