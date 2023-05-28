def calular_nota(nota):
    if nota >= 7:
        return "Aprovado"
    else:
        return "Reprovado"


def exibir_lista_geral():
    for aluno in alunos:
        print('Nome', aluno['nome'])
        print("Nota:", aluno["nota"])
        print("Status:", aluno["status"])
        print()


def exibir_lista_reprovados():
    print('Alunos reprovados:')
    for aluno in reprovados:
        print(aluno)


quantidade_de_alunos = int(input('Informe a quantidade de alunos: '))
alunos = []
reprovados = []

for i in range(quantidade_de_alunos):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    status = calular_nota(nota)
    alunos.append({"nome": nome, "nota": nota, "status": status})
    if status == 'Reprovado':
        reprovados.append(nome)


exibir_lista_geral()
exibir_lista_reprovados()
