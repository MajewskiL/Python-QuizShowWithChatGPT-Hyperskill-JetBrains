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


def unpack_facts(facts):
    facts_list = [data.strip() for data in facts.split(mark)[1:]]
    return facts_list


topic = input("Enter the quiz topic: ")

#  Stage 3 check if lines starts with bullets and has all facts, last stage facts - if good answer, questions changed
mark = "TaskMark:"
chat_question_1 = (f"Print four short facts about {topic} line by line, without bullet points, and each fact should have prefix '{mark}'.")
chat_answer_1 = ask_chat(chat_question_1)
print(chat_answer_1)
chat_data_1 = unpack_facts(chat_answer_1)

i = 0
while True:
    print("Menu:")
    print("1) Facts")
    print("2) Exit")
    print("3) Quiz")
    ans = int(input("Choose: "))
    if ans == 2:
        exit()
    elif ans == 1:
        while True:
            i = i % len(chat_data_1)
            print(f"Fact: {chat_data_1[i]}")
            ans2 = input("Do you want next fact (y/n)? ")
            if ans2.lower() == "y":
                i += 1
                continue
            elif ans2.lower() == "n":
                i += 1
                break
            else:
                print("Unknown choice.")
    else:
        print("Unknown choice.")
