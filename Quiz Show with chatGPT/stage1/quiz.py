from openai import OpenAI
import os

API_KEY = os.environ.get('API_KEY')


def ask_chat(q):
    client = OpenAI(api_key=API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        messages=[
            {
                "role": "user",
                "content": f"{q}"
            }
        ],
    )
    answer = response.choices[0].message.content
    return answer


topic = input("Enter the quiz topic: ")

#  Stage 1
chat_question_1 = (f"Give one short fact about {topic}.")
chat_answer_1 = ask_chat(chat_question_1)
print(chat_answer_1)
