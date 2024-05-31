from gemini import get_abstract, get_questions
from read_file import extract_text
from time import sleep
import os


vetor = [''] * 2

def print_title():
    print("""
$$$$$$$$\                     $$\           $$\           $$\  $$$$$$\            
$$  _____|                    $$ |          \__|          \__|$$  __$$\           
$$ |      $$\   $$\  $$$$$$\  $$ | $$$$$$\  $$\ $$$$$$$\  $$\ $$ /  \__|$$\   $$\ 
$$$$$\    \$$\ $$  |$$  __$$\ $$ | \____$$\ $$ |$$  __$$\ $$ |$$$$\     $$ |  $$ |
$$  __|    \$$$$  / $$ /  $$ |$$ | $$$$$$$ |$$ |$$ |  $$ |$$ |$$  _|    $$ |  $$ |
$$ |       $$  $$<  $$ |  $$ |$$ |$$  __$$ |$$ |$$ |  $$ |$$ |$$ |      $$ |  $$ |
$$$$$$$$\ $$  /\$$\ $$$$$$$  |$$ |\$$$$$$$ |$$ |$$ |  $$ |$$ |$$ |      \$$$$$$$ |
\________|\__/  \__|$$  ____/ \__| \_______|\__|\__|  \__|\__|\__|       \____$$ |
                    $$ |                                                $$\   $$ |
                    $$ |                                                \$$$$$$  |
                    \__|                                                 \______/
""")


def loading():
    i = 0
    while i <= 80:
        print('#', end="", flush=True)
        i += 1
        sleep(0.2)


def menu():
    print("""
[1] - Pedir resumo de um PDF
[2] - Pedir perguntas de um PDF
[3] - Ver resumo
[4] - Ver questões
[5] - Sair
""")
    op = int(input("O que deseja ? "))
    return op 


def print_content_vetor(n):
    if vetor[n] == '':
        if n == 0:
            os.system("cls")
            print("Não há resumos gerados")
            sleep(2)

        else:
            os.system("cls")
            print("Não há quetões geradas")
            sleep(2)
            
    else:
        os.system("cls")
        print(vetor[n]) 
        input("Enter para o menu: ")
        sleep(1)
        os.system('cls')


print_title()
loading()
while True:
    op = menu()
    if op == 1 or op == 2:
        file = str(input("Digite o caminho do arquivo: "))
        topic = str(input("Algum tópico especifico(Enter caso não queira): "))
        text = extract_text(file)
    match op:
        case 1:
            os.system("cls")
            print("Aguarde")
            abstract = get_abstract(text, topic)
            vetor[0] = abstract
            print("Resumo gerado.")
            sleep(3)
            os.system("cls")
            print_title()
        case 2:
            count = input("Número de questões: ")
            os.system("cls")
            print("Aguarde")
            if count !=  "":
                questios = get_questions(text, topic, int(count))
            else:
                questios = get_questions(text, topic)
            os.system("cls")
            print("Aguarde")
            vetor[1] = questios
            print("Questões geradas")
            sleep(3)
            os.system("cls")
            print_title()
        case 3:
            print_content_vetor(0)
            print_title()
        case 4:
            print_content_vetor(1)
            print_title()     
        case 5:
            break
        case _:
            os.system("cls") 
            print("Opção inválida")
            sleep(2)
            os.system("cls")
            print_title()         
    


    
