def calcular_status_aluno(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

alunos = []
for i in range(quantidade_alunos):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    status = calcular_status_aluno(nota)
    alunos.append({"nome": nome, "nota": nota, "status": status})

# Exibir informações dos alunos
for aluno in alunos:
    print("Nome:", aluno["nome"])
    print("Nota:", aluno["nota"])
    print("Status:", aluno["status"])
    print()
