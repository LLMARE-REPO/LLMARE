import requests
import json
from openai import OpenAI
import httpx
#API_KEY = "sk-a1YKVib9zVBgRjuYFe70225b6a9b4e97A2DaE051D7F0A29c"
#和gpt进行交互
api_key = 'sk-bkOEKBKIerfse6cEE5F1FaF68dC64b51A18c709a1aCb2577'


def ask_llama(prompt):
    # 使用 DeepSeek API 进行问答
    client = OpenAI(api_key="sk-odpBDa8L312TH9Pt1bCa8bDaA6F24813B748Df094748D70a", base_url="https://hk.xty.app/v1")

    response = client.chat.completions.create(
        model="llama-3.1-nemotron-ultra-253b-v1",
        messages=[
            {"role": "system", "content": "You are a mobile application tester and are currently attempting to reproduce the functional scenarios that need improvement as mentioned by users in the application reviews."},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def ask_gpt_oss(prompt):
    # 使用 DeepSeek API 进行问答
    client = OpenAI(api_key="sk-odpBDa8L312TH9Pt1bCa8bDaA6F24813B748Df094748D70a", base_url="https://hk.xty.app/v1")

    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "system", "content": "You are a mobile application tester and are currently attempting to reproduce the functional scenarios that need improvement as mentioned by users in the application reviews."},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def ask_deepseek(prompt):
    # 使用 DeepSeek API 进行问答
    client = OpenAI(api_key="sk-8373fc19683c487989b65337bb194efb", base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-reasoner",
        messages=[
            {"role": "system", "content": "You are a mobile application tester and are currently attempting to reproduce the functional scenarios that need improvement as mentioned by users in the application reviews."},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

def ask_qwen(prompt):
    try:
        # 使用 DeepSeek API 进行问答
        client = OpenAI(api_key="sk-7418a17f9bfb4ada8e9de28bf0f6ed54", base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

        response = client.chat.completions.create(
            # model="qwen3-235b-a22b",
            # model="qwen3-235b-a22b-thinking-2507",
            model = "qwen3-next-80b-a3b-thinking",
            messages=[
                {"role": "system", "content": "You are a mobile application tester and are currently attempting to reproduce the functional scenarios that need improvement as mentioned by users in the application reviews."},
                {"role": "user", "content": prompt},
            ],
            # extra_body={"enable_thinking": False},
            stream=False
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    except Exception as e:
        print("Error:", e)
        return None



'''
def ask_gpt(content):
    payload = {
        "model": configs["OPENAI_API_MODEL"],
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "temperature": configs["TEMPERATURE"],
        "max_tokens": configs["MAX_TOKENS"]
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {configs['OPENAI_API_KEY']}"
    }
    r = requests.post(configs["OPENAI_API_BASE"], headers=headers, json=payload)
    if r.status_code == 200:
        message = (json.loads(r.text))["choices"][0]["message"]["content"]
        #print(message)
        return message
    else:
        print(r.status_code)
        return False
'''
'''
def ask_gpt(content):
    client = OpenAI(api_key="none", base_url="http://222.20.126.133:8000/v1")
    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "user", "content": content}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content
'''

def ask_gpt_info(content):
    client = OpenAI(
        base_url="https://hk.xty.app/v1",
        api_key= api_key,  # 3.5
        #api_key="oqgFbxqHulqJGfUiAbE1De00066145E4AcF0D5BaC569F573",
        http_client=httpx.Client(
            base_url="https://hk.xty.app/v1",
            follow_redirects=True,
        ),
    )

    completion = client.chat.completions.create(
        #model="gpt-3.5-turbo",
        model="gpt-4o-mini",
        #model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": content},
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def ask_gpt_state(content):
    client = OpenAI(
        base_url="https://hk.xty.app/v1",
        #api_key="sk-NEI39Ft0cx0sezU8914aE7D447114662817cC404106984Ea",  # 3.5
        api_key= api_key,
        http_client=httpx.Client(
            base_url="https://hk.xty.app/v1",
            follow_redirects=True,
        ),
    )

    completion = client.chat.completions.create(
        #model="gpt-3.5-turbo",
        model="gpt-4o",
        #model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": content},
        ],
        n=1,
        stop=None,
        #max_tokens=2000
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def ask_gpt_activity(content):
    client = OpenAI(
        base_url="https://hk.xty.app/v1",
        #api_key="sk-NEI39Ft0cx0sezU8914aE7D447114662817cC404106984Ea",  # 3.5
        api_key=api_key,
        http_client=httpx.Client(
            base_url="https://hk.xty.app/v1",
            follow_redirects=True,
        ),
    )

    completion = client.chat.completions.create(
        #model="gpt-3.5-turbo",
        model="gpt-4o",
        #model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": content},
        ],
        n=1,
        stop=None,
        # max_tokens = 2000
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def ask_gpt(content):
    client = OpenAI(
        base_url="https://hk.xty.app/v1",
        api_key=api_key,  # 3.5
        #api_key="sk-GALXPOOXbzJ7ZCeR682bFd7583Ca4fFe8d62D04706D1009f",
        http_client=httpx.Client(
            base_url="https://hk.xty.app/v1",
            follow_redirects=True,
        ),
    )

    completion = client.chat.completions.create(
        #model="gpt-3.5-turbo",
        model="gpt-4o",
        #model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": content},
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def ask_gpt_4(content):
    client = OpenAI(
        base_url="https://hk.xty.app/v1",
        # api_key="sk-KwToDClZk6kf37pxF0397bD8B47a4d5eB53911408e8964F1",  # 3.5
        api_key=api_key,
        http_client=httpx.Client(
            base_url="https://hk.xty.app/v1",
            follow_redirects=True,
        ),
    )

    completion = client.chat.completions.create(
        #model="gpt-4-turbo-preview",
        model="gpt-4o",
        #model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": content},
        ],
        n=1,
        stop=None,
        #max_tokens=2000
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


def ask_gpt4(content):
    while True:
        try:
            client = OpenAI(
                base_url="https://api.xty.app/v1",
                #base_url="https://hk.xty.app/v1",
                # api_key="sk-KwToDClZk6kf37pxF0397bD8B47a4d5eB53911408e8964F1",  # 3.5
                api_key=api_key,
                http_client=httpx.Client(
                    base_url="https://api.xty.app/v1",
                    follow_redirects=True,
                ),
            )

            completion = client.chat.completions.create(
                #model="gpt-4-turbo-preview",
                model="gpt-4o",
                #model="claude-3-5-sonnet-20240620",
                messages=[
                    {"role": "user", "content": content},
                ],
                n=1,
                stop=None,
                #max_tokens=2000
            )
            print(completion.choices[0].message.content)
            break
        except:
            pass
    return completion.choices[0].message.content

def ask_gpt4mini(content):
    client = OpenAI(
        base_url="https://api.xty.app/v1",
        # api_key="sk-KwToDClZk6kf37pxF0397bD8B47a4d5eB53911408e8964F1",  # 3.5
        api_key=api_key,
        http_client=httpx.Client(
            base_url="https://api.xty.app/v1",
            follow_redirects=True,
        ),
    )

    completion = client.chat.completions.create(
        #model="gpt-4-turbo-preview",
        model="gpt-4o-mini",
        #model="claude-3-5-sonnet-20240620",
        messages=[
            {"role": "user", "content": content},
        ],
        #max_tokens=2000
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content