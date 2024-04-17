from openai import OpenAI
import os

API_KEY = os.environ.get('API_KEY')
TOPIC_MARK = "TaskMark:"
QUESTION_MARK = "QuestionMark:"
ANSWER_MARK = "AnswerMark:"
DIVISION_MARK = "DivisionMark"

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


def unpack_answer(facts, prefix):
    facts_list = [data.strip() for data in facts.split(prefix)[1:]]
    return facts_list


def generate_facts(topic):
    chat_question_1 = (
        f"Print four short facts about {topic} line by line, without bullet points, and each fact should have prefix '{TOPIC_MARK}'.")
    return ask_chat(chat_question_1)


def generate_questions(facts):
    chat_question_2 = (
        f"Print one question for each facts from list: {','.join(facts)}, "
        f"using different words as are in fact,"
        f"where two of them should have answer 'true' and two of them should have answer 'false',"
        f"printed line by line, "
        f"without bullet points, "
        f"and each question should have prefix '{QUESTION_MARK}' and sufix {ANSWER_MARK} with answer.")
    return ask_chat(chat_question_2)


def menu():
    facts = str()
    facts_list = list()
    while True:
        print("Menu:")
        print("(F)acts generator")
        print("(L)earn facts")
        print("(E)xit")
        ans = input("Choose: ").lower()
        if ans == "e":
            return
        elif ans == "f":
            topic = input("Enter the quiz topic: ")
            facts = generate_facts(topic)
            print(facts)
            print(DIVISION_MARK)
            facts_list = unpack_answer(facts, TOPIC_MARK)
            question_list = generate_questions(facts_list)
            print(question_list)
            print()
        elif ans == "l":
            for i, fact in enumerate(facts_list):
                print(f"{i + 1}) {fact}")
            print('')
        else:
            print("Unknown command.\n")


#  Stage 3 - q1: python os library
# tak genrować, żeby były i true i false - najlepiej randomly
# podzielić przez DivisionMark na 2, każde inny przez TaskMark i QuestionMark na 4, i Question przez AnswerMark na 2
menu()
