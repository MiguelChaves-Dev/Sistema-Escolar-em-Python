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
        nome = input("Insira o nome do Aluno: ")
        aluno["Nome"] = {}
        aluno["Nome"][nome] = {}
        aluno["Nome"][nome]["Classe"] = input("Insira a classe atual do Aluno: ")
        aluno["Nome"][nome]["Idade"] = int(input("Insira a idade do Aluno: "))
        alunos.append(aluno)
        pergunta = input("Deseja cadastrar outro aluno? (s/n): ")
        if pergunta.lower() != "s":
            break
    with open("Alunos.json", "w", encoding="utf-8") as arq:
        json.dump(alunos, arq, indent=4, ensure_ascii=False)

def boletim():
    while True:
        with open("Alunos.json", "r", encoding="utf-8") as arq:
            dados = json.load(arq)
        print("")
        pergunta = input("Qual aluno você quer alterar as notas?")
        print("")
        print("[1] 1° Bimestre")
        print("[2] 2° Bimestre")
        print("[3] 3° Bimestre")
        print("[4] 4° Bimestre")
        opcao = int(input("Qual bimestre você deseja adicionar as notas?: "))
        encontrado = False
        for aluno in dados:
            if pergunta in aluno["Nome"]:
                encontrado = True
                match opcao:
                    case 1:
                        aluno["Nome"][pergunta]["1° Bimestre"] = {}
                        aluno["Nome"][pergunta]["1° Bimestre"]["Nota1"] = float(input("Insira a primeira nota: "))
                        aluno["Nome"][pergunta]["1° Bimestre"]["Nota2"] = float(input("Insira a segunda nota: "))
                        aluno["Nome"][pergunta]["1° Bimestre"]["Nota3"] = float(input("Insira a terceira nota: "))
                        aluno["Nome"][pergunta]["1° Bimestre"]["Nota4"] = float(input("Insira a quarta nota:"))
                        with open("Alunos.json", "w", encoding="utf-8") as arq:
                            json.dump(dados, arq, indent=4, ensure_ascii=False)
                        print("Notas Adicionadas com Sucesso!")
                        break
                    case 2:
                        aluno["Nome"][pergunta]["2° Bimestre"] = {}
                        aluno["Nome"][pergunta]["2° Bimestre"]["Nota1"] = float(input("Insira a primeira nota: "))
                        aluno["Nome"][pergunta]["2° Bimestre"]["Nota2"] = float(input("Insira a segunda nota: "))
                        aluno["Nome"][pergunta]["2° Bimestre"]["Nota3"] = float(input("Insira a terceira nota: "))
                        aluno["Nome"][pergunta]["2° Bimestre"]["Nota4"] = float(input("Insira a querta nota: "))
                        with open("Alunos.json", "w", encoding="utf-8") as arq:
                            json.dump(dados, arq, indent=4, ensure_ascii=False)
                        print("Notas Adicionadas com Sucesso!")
                        break
                    case 3:
                        aluno["Nome"][pergunta]["3° Bimestre"] = {}
                        aluno["Nome"][pergunta]["3° Bimestre"]["Nota1"] = float(input("Insira a primeira nota: "))
                        aluno["Nome"][pergunta]["3° Bimestre"]["Nota2"] = float(input("Insira a segunda nota: "))
                        aluno["Nome"][pergunta]["3° Bimestre"]["Nota3"] = float(input("Insira a terceira nota: "))
                        aluno["Nome"][pergunta]["3° Bimestre"]["Nota4"] = float(input("Insira a quarta nota: "))
                        with open("Alunos.json", "w", encoding="utf-8") as arq:
                            json.dump(dados, arq, indent=4, ensure_ascii=False)
                        print("Notas Adicionadas com Sucesso!")
                        break
                    case 4:
                        aluno["Nome"][pergunta]["4° Bimestre"] = {}
                        aluno["Nome"][pergunta]["4° Bimestre"]["Nota1"] = float(input("Insira a primeira nota: "))
                        aluno["Nome"][pergunta]["4° Bimestre"]["Nota2"] = float(input("Insira a segunda nota: "))
                        aluno["Nome"][pergunta]["4° Bimestre"]["Nota3"] = float(input("Insira a terceira nota: "))
                        aluno["Nome"][pergunta]["4° Bimestre"]["Nota4"] = float(input("Insira a quarta nota: "))
                        with open("Alunos.json", "w", encoding="utf-8") as arq:
                            json.dump(dados, arq, indent=4, ensure_ascii=False)
                        print("Notas Adicionadas com Sucesso!")
                        break
                    case _:
                        print("Insira um bimestre válido!")
        if not encontrado:
            print(f"O aluno {pergunta} não foi encontrado!")
        continuar = input("Deseja cadastrar outra nota?: ")
        if continuar != "s":
            break
def visualização():
    while True:
        with open("Alunos.json", "r", encoding="utf-8") as arq:
            dados = json.load(arq)
        pergunta = input("Qual aluno você deseja visualizar o boletim?: ")
        encontrado = False
        for aluno in dados:
            if pergunta in aluno["Nome"]:
                encontrado = True
                b1n1 = aluno["Nome"][pergunta]["1° Bimestre"]["Nota1"]
                b1n2 = aluno["Nome"][pergunta]["1° Bimestre"]["Nota2"]
                b1n3 = aluno["Nome"][pergunta]["1° Bimestre"]["Nota3"]
                b1n4 = aluno["Nome"][pergunta]["1° Bimestre"]["Nota4"]
                b2n1 = aluno["Nome"][pergunta]["2° Bimestre"]["Nota1"]
                b2n2 = aluno["Nome"][pergunta]["2° Bimestre"]["Nota2"]
                b2n3 = aluno["Nome"][pergunta]["2° Bimestre"]["Nota3"]
                b2n4 = aluno["Nome"][pergunta]["2° Bimestre"]["Nota4"]
                b3n1 = aluno["Nome"][pergunta]["3° Bimestre"]["Nota1"]
                b3n2 = aluno["Nome"][pergunta]["3° Bimestre"]["Nota2"]
                b3n3 = aluno["Nome"][pergunta]["3° Bimestre"]["Nota3"]
                b3n4 = aluno["Nome"][pergunta]["3° Bimestre"]["Nota4"]
                b4n1 = aluno["Nome"][pergunta]["4° Bimestre"]["Nota1"]
                b4n2 = aluno["Nome"][pergunta]["4° Bimestre"]["Nota2"]
                b4n3 = aluno["Nome"][pergunta]["4° Bimestre"]["Nota3"]
                b4n4 = aluno["Nome"][pergunta]["4° Bimestre"]["Nota4"]
                print("1° Bimestre -------2° Bimestre ------- 3° Bimestre ------- 4°Bimestre")
                print(f"  {b1n1} --------------{b2n1} ------------{b3n1} --------------{b4n1}")
                print(f"  {b1n2} --------------{b2n2} ------------{b3n2} --------------{b4n2}")
                print(f"  {b1n3} --------------{b2n3} ------------{b3n3} --------------{b4n3}")
                print(f"  {b1n4} --------------{b2n4} ------------{b3n4} --------------{b4n4}")
                print()
            continuar = input("Deseja visualizar outro boletim?: ")
           
        if not encontrado:
            print(f"O aluno {pergunta} não foi encontrado!")
        if continuar != "s":
            break        
    
def verificação():
    with open("Alunos.json", "r", encoding="utf-8") as arq:
        dados = json.load(arq)
    print("")
    print("")
    pergunta = input("Qual aluno você deseja verificar o cadastro?: ")
    encontrado = False
    for aluno in dados:
        if pergunta in aluno["Nome"]:
            print(f"Nome: {pergunta}")
            print(f"Classe: {aluno['Nome'][pergunta]['Classe']}")
            print(f"Idade: {aluno['Nome'][pergunta]['Idade']}")
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
        if pergunta in aluno["Nome"]:
            dados.remove(aluno)
            print(f"Aluno {pergunta} removido com sucesso!")
            encontrado = True
            break
    if not encontrado:
        print(f"O aluno {pergunta} não foi encontrado!")
    with open("Alunos.json", "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)