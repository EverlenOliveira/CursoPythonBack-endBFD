# cadastro_alunos.py

alunos = []

def cadastrar_aluno():
    print("\n--- Cadastro de Aluno ---")
    nome = input("Digite o nome do aluno: ")
    curso = input("Digite o curso do aluno: ")

    while True:
        try:
            matricula = int(input("Digite o número da matrícula (somente números): "))

            if any(aluno["matricula"] == matricula for aluno in alunos):
                print("Essa matrícula já está cadastrada! Digite outro número.")
                continue

            break
        except ValueError:
            print("Matrícula inválida! Digite apenas números.")

    aluno = {"nome": nome, "matricula": matricula, "curso": curso}
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")
    input("Pressione ENTER para continuar...")


def listar_alunos():
    print("\n--- Alunos Cadastrados ---")
    if not alunos:
        print("Nenhum aluno cadastrado.\n")
    else:
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. Nome: {aluno['nome']} | Matrícula: {aluno['matricula']} | Curso: {aluno['curso']}")
        print()
    input("Pressione ENTER para continuar...")


def buscar_aluno():
    print("\n--- Buscar Aluno ---")
    try:
        matricula = int(input("Digite a matrícula do aluno que deseja buscar: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")
        input("Pressione ENTER para continuar...")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Aluno encontrado: Nome: {aluno['nome']} | Curso: {aluno['curso']}\n")
            input("Pressione ENTER para continuar...")
            return
    print("Aluno não encontrado.\n")
    input("Pressione ENTER para continuar...")


def remover_aluno():
    print("\n--- Remover Aluno ---")
    try:
        matricula = int(input("Digite a matrícula do aluno que deseja remover: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")
        input("Pressione ENTER para continuar...")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            alunos.remove(aluno)
            print(f"Aluno {aluno['nome']} removido com sucesso!\n")
            input("Pressione ENTER para continuar...")
            return

    print("Aluno não encontrado.\n")
    input("Pressione ENTER para continuar...")


def editar_aluno():
    print("\n--- Editar Aluno ---")
    try:
        matricula = int(input("Digite a matrícula do aluno que deseja editar: "))
    except ValueError:
        print("Entrada inválida! Digite apenas números.\n")
        input("Pressione ENTER para continuar...")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            print(f"Aluno encontrado: Nome: {aluno['nome']} | Curso: {aluno['curso']}")
            novo_nome = input("Digite o novo nome (ou pressione ENTER para manter): ")
            novo_curso = input("Digite o novo curso (ou pressione ENTER para manter): ")

            if novo_nome.strip():
                aluno["nome"] = novo_nome
            if novo_curso.strip():
                aluno["curso"] = novo_curso

            print("Dados do aluno atualizados com sucesso!\n")
            input("Pressione ENTER para continuar...")
            return

    print("Aluno não encontrado.\n")
    input("Pressione ENTER para continuar...")


def sair():
    print("\nSaindo do sistema... Até mais!")
    exit()

def exibir_menu():
    print("==== Sistema de Cadastro de Alunos ====")
    print("1 - Cadastrar Novo Aluno")
    print("2 - Listar Alunos Cadastrados")
    print("3 - Buscar Aluno por Matrícula")
    print("4 - Remover Aluno por Matrícula")
    print("5 - Editar Aluno por Matrícula")
    print("6 - Sair")
    return input("Escolha uma opção: ")


def main():
    opcoes = {
        "1": cadastrar_aluno,
        "2": listar_alunos,
        "3": buscar_aluno,
        "4": remover_aluno,
        "5": editar_aluno,
        "6": sair
    }

    while True:
        escolha = exibir_menu()
        funcao = opcoes.get(escolha)
        if funcao:
            funcao()
        else:
            print("Opção inválida! Tente novamente.\n")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()