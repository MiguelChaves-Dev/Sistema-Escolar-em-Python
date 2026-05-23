import Funcoes

while True:
    print("[1]Cadastrar um Aluno")
    print("[2]Verificar Cadastro de Aluno")
    print("[3]Remover Aluno")
    print("[4]Encerrar Programa")
    opcao = int(input("O que você deseja fazer?: "))
    match opcao:
        case 1:
            Funcoes.cadastro()
        case 2:
            Funcoes.verificação()
        case 3:
            Funcoes.remoção()
        case 4:
            print("Encerrando...")
            break