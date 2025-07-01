import random


def open_file(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    # Разбиваем по двойным переходам строки — каждый блок вопрос + ответ
    blocks = [block.strip() for block in content.split('\n\n') if block.strip()]

    questions = []
    i = 0
    while i < len(blocks):
        question = blocks[i]
        i += 1
        answer_parts = []
        # собираем все последующие блоки, пока не встретим новый вопрос (т.е. следующий блок — вопрос)
        # по формату файла вопрос начинается с новой строки без отступа
        # каждый второй блок — ответ
        if i < len(blocks):
            answer = blocks[i]
            i += 1
        else:
            answer = ''
        questions.append({'question': question, 'answer': answer})

    return questions


def rand_quest(questions, count=10):
    if len(questions) < count:
        count = len(questions)
    return random.sample(questions, count)
