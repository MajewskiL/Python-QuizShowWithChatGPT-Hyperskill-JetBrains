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


def unpack_questions(questions, facts):
    questions_list = [data.strip() for data in questions.split(QUESTION_MARK)[1:]]
    questions_list = [data.split(ANSWER_MARK) for data in questions_list]
    questions_list = [[facts[i], questions_list[i][0], True]
                      if questions_list[i][1].strip().lower() == "true"
                      else [facts[i], questions_list[i][0], False]
                      for i in range(len(questions_list))]
    return questions_list


def generate_facts(topic):
    chat_question_1 = (
        f"Print four short facts about {topic} line by line, without bullet points, and each fact should have prefix '{TOPIC_MARK}'.")
    return ask_chat(chat_question_1)


def generate_questions(facts):
    chat_question_2 = (
        f"Print one question for each facts from list: {','.join(facts)} "
        f"using different words as are in fact,"
        f"where two of them should have answer 'true' and two of them should have answer 'false',"
        f"printed line by line, "
        f"without bullet points, "
        f"and each question should have prefix '{QUESTION_MARK}' and sufix {ANSWER_MARK} with answer.")
    return ask_chat(chat_question_2)


def quiz(questions_list):
    while len(questions_list) != 0:
        for question in questions_list:
            print(f"{question[1]} false/true: ")
            ans = input()
            ans = True if ans.lower().strip() == "true" else False
            if ans == question[2]:
                print("Correct!")
                questions_list.remove(questions_list.index(question))
            else:
                new_question = (f"Generate new question with answer not {question[2]} for fact: '{question[0]}' "
                                f"different than '{question[1]}'")
                new_question = ask_chat(new_question)
                questions_list[questions_list.index(question)] = [question[0], new_question, not question[2]]
    return


def menu():
    facts = str()
    facts_list = list()
    questions = str()
    questions_list = list()
    while True:
        print("Menu:")
        print("(F)acts generator")
        print("(L)earn facts")
        print("(Q)uiz Show")
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
            questions = generate_questions(facts_list)
            print(questions)
            print()
        elif ans == "l":
            for i, fact in enumerate(facts_list):
                print(f"{i + 1}) {fact}")
            print('')
        elif ans == "q":
            quiz(unpack_questions(questions, facts_list))
        else:
            print("Unknown command.\n")


#  Stage 3 - q1: python os library
# tak genrować, żeby były i true i false - najlepiej randomly
menu()

'''lista = ["egg", "duck", "smoke", "cherry", "train", "home", "hedge", "plain", "sun", "rocks", "fish", "boat", "Santana"]
for l in lista:
    f1 = generate_facts(l)
    f2 = unpack_answer(f1, TOPIC_MARK)
    f3 = generate_questions(f2)
    f4 = unpack_questions(f3)
    #print([True if j[1].strip().lower() == "true" else False for j in f4])
    print(f'{all([True if j[1].strip().lower() == "true" else False for j in f4])} | {any([j[1] for j in f4])}')
#menu()'''


# Stage 4 - q1: python os library
# pytamy tak długa jak nie exit lub nie udzielono poprwnych odpowiedzi. Każda poprawna usuwa pytanie.
# Każda zła zamienia pytanie i nie mogą się powtarzać - do trzech. - najlepiej by było losowo true/false
# ale na potrzeby testów robimy oposite.

