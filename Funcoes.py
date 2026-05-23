import json

try:
    with open("Alunos.json", "r", encoding="utf-8") as arq:
        alunos = json.load(arq)
except (FileNotFoundError, json.JSONDecodeError):
    alunos = []
    
def cadastro():
    while True:
        aluno = {}
        print("")
        print("")
        aluno["Nome"] = input("Insira o nome do Aluno: ")
        aluno["Classe"] = input("Insira a classe atual do Aluno: ")
        aluno["Idade"] = int(input("Insira a idade do Aluno: "))
        alunos.append(aluno)
        pergunta = input("Deseja cadastrar outro aluno? (s/n): ")
        if pergunta.lower() != "s":
            break
    with open("Alunos.json", "w", encoding="utf-8") as arq:
        json.dump(alunos, arq, indent=4, ensure_ascii=False)

def verificação():
    with open("Alunos.json", "r", encoding="utf-8") as arq:
        dados = json.load(arq)
    print("")
    print("")
    pergunta = input("Qual aluno você deseja verificar o cadastro?: ")
    encontrado = False
    for aluno in dados:
        if aluno["Nome"].lower() == pergunta.lower():
            print(f"Nome: {aluno['Nome']}")
            print(f"Classe: {aluno['Classe']}")
            print(f"Idade: {aluno['Idade']}")
            encontrado = True
            break
    if not encontrado:
        print(f"O aluno {pergunta} não está cadastrado!")

def remoção():
    with open("Alunos.json", "r", encoding="utf-8") as arq:
        dados = json.load(arq)
    print("")
    print("")
    pergunta = input("Qual aluno você deseja remover o cadastro?: ")
    encontrado = False
    for aluno in dados:
        if aluno["Nome"].lower() == pergunta.lower():
            dados.remove(aluno)
            print(f"Aluno {pergunta} removido com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print(f"O aluno {pergunta} não foi encontrado!")
    with open("Alunos.json", "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)