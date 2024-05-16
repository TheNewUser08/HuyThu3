# Example: reuse your existing OpenAI setup
from openai import OpenAI
# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
with open('prompt.txt') as f:
    systemPrompt = f.read()
def get_response(user_input, username):
    lowered = user_input.lower()
    if lowered == "":
        return "nothing?"

    content = f'You are talking to {username}, {lowered}'

    translationVE = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
            {"role": "system",
             "content": "You will translate the follow text to English, just translate it, no explanation"},
            {"role": "user", "content": f"Translate this to English, translate 'mày' and 'm' to 'you': {content}"
             }
        ],
        temperature=0.7,
    )
    noidungtienganh = translationVE.choices[0].message.content
    print(noidungtienganh)
    history = [{"role": "system", "content": systemPrompt},
               {"role": "user", "content": noidungtienganh},
               ]
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=history,
        temperature=0.8,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}

    for chunk in completion:
        if chunk.choices[0].delta.content:
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)

    noidung = new_message["content"]
    translationEV = client.chat.completions.create(
        model="Orenguteng/Llama-3-8B-Lexi-Uncensored-GGUF",
        messages=[
            {"role": "system", "content": "Bạn là một trợ lí và sẽ dịch tiếng anh sang tiếng việt một cách chuẩn xác. Dịch 'I' thành 'Tao'. dịch 'you' thành 'mày', chỉ dịch chứ không thêm nội dung"},
            {"role": "user", "content": f"Dịch 'I' thành 'Tao'. dịch 'you' thành 'mày' và Dịch phần sau đây sang tiếng việt, chỉ dịch chứ không thêm nội dung: {noidung}"
}
        ],
        temperature=0.7,
    )
    print(noidung)
    return translationEV.choices[0].message.content

