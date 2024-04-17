from openai import OpenAI
import os

API_KEY = os.environ.get('API_KEY')
TOPIC_MARK = "TaskMark:"


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


def generate_facts(topic):
    chat_question_1 = (
        f"Print four short facts about {topic} line by line, without bullet points, and each fact should have prefix '{TOPIC_MARK}'.")
    print("Facts was generated by AI!")
    return ask_chat(chat_question_1)


def menu():
    facts = list()
    while True:
        print("\nMenu:")
        print("(G)enerate facts")
        print("(F)acts")
        print("(E)xit")
        ans = input("Choose: ").lower()
        if ans == "e":
            return
        elif ans == "g":
            topic = input("Enter the quiz topic: ")
            facts = [generate_facts(topic)]
        elif ans == "f":
            print(facts[0])
        else:
            print("Unknown command.")


#  Stage 2 - q1: python os library
menu()
