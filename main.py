import google.generativeai as genai
from read_file import extract_text


genai.configure(api_key="AIzaSyBXmDwXVihvovzRUl6J9l0XDStzrezWIjA")

model = genai.GenerativeModel(model_name="gemini-pro")

def get_abstract(text, topic = ''):
    if topic == '':
        abstract = model.generate_content(f'com base no texto abaixo produza um resumo, ele deve ser didático, objetivo e claro. Conceitue cada tópico de forma detalhada. Além disso, forneça exemplos práticos para melhor entendimento: \n {text}')

        return abstract.text
    else:
        abstract = model.generate_content(f'com base no texto abaixo, busque pelo tópico {topic} e produza um resumo, ele deve ser didático, objetivo e claro. Conceitue cada tópico de forma detalhada. Além disso, forneça exemplos práticos para melhor entendimento: \n {text}')

        return abstract.text


def get_questions(text, topic = '', count = 5):
    if topic == '':
        question = model.generate_content(f'Com base no texto abaixo produza {count} questões com alternativas com foco no aprendizado do contéudo proposto, faça questões inspiradas nas de concurso com alternativas(mescle a dificuldade das questões, mas não mostre a dificuldade): \n {text}')

        return question.text
    else:
        question = model.generate_content(f'Com base no texto abaixo busque pelo tópico {topic} e produza {count} questões com alternativas com foco no aprendizado do tópico proposto, faça questões inspiradas nas de concurso com alternativas(mescle a dificuldade das questões, mas não mostre a dificuldade): \n {text}')

        return question.text





text = extract_text("Estrutura_de_dados.pdf")

print(get_questions(text, 'fila'))