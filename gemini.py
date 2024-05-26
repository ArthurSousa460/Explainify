import google.generativeai as genai


genai.configure(api_key="AIzaSyBXmDwXVihvovzRUl6J9l0XDStzrezWIjA")

model = genai.GenerativeModel(model_name="gemini-pro")

chat = model.start_chat()

def get_abstract(text, topic = ''):
    if topic == '':
        abstract = chat.send_message(f'com base no texto abaixo produza um resumo, ele deve ser didático, objetivo e claro. Conceitue cada tópico de forma detalhada. Além disso, forneça exemplos práticos para melhor entendimento: \n {text}')

        return abstract.text
    else:
        abstract = chat.send_message(f'com base no texto abaixo, busque pelo tópico {topic} e produza um resumo, ele deve ser didático, objetivo e claro. Conceitue cada tópico de forma detalhada. Além disso, forneça exemplos práticos para melhor entendimento: \n {text}')

        return abstract.text


def get_questions(text, topic = '', count = 5):
    if topic == '':
        question = chat.send_message(f'Com base no texto abaixo produza {count} questões com alternativas com foco no aprendizado do contéudo proposto, faça questões inspiradas nas de concurso com com questões de multipla escolha(mescle a dificuldade das questões, mas não mostre a dificuldade) e gere o gabarito. Texto: \n {text}')

        return question.text
    else:
        question = chat.send_message(f'Com base no texto abaixo busque pelo tópico {topic} e produza {count} questões com alternativas com foco no aprendizado do tópico proposto, faça questões inspiradas nas de concurso com questões de multipla escolha(mescle a dificuldade das questões, mas não mostre a dificuldade) e gere o gabarito. Texto: \n {text}')

        return question.text



