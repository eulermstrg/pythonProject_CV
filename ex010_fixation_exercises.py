# Exercício de fixação:
#
# Peça para o usuário digitar seu nome
# Peça para o usuário digitar sua idade
#
# Se nome e idade forem digitados:
#     Exiba:
#         Seu nome é:
#         Seu nome invertido é:
#         A primeira letra do seu nome é:
#         Sua idade é:
#         Seu nome contém (ou não) espaços
#         A última letra do seu nome é:
#
# Se nada for digitado em nome ou idade:
#     Exiba:
#         'Desculpe, você deixou campos vazios.'

while True:
    nome = input('Digite seu nome: ')
    idade: str = input('Digite sua idade:')
    res = " " in nome
    size = len(nome)

    if nome and idade:
        print(f'Seu nome é: {nome}')
        print(f'Seu nome invertido é: {nome[len(nome)::-1]} ')
        print(f'A última letra do seu nome é: {nome[len(nome)-1:len(nome):]}')
        print(f'A primeira letra do seu nome é: {nome[0:1:]}')
        print(f'Sua idade é: {idade}')

        if not res:
            print('Seu nome não contém espaços.')
        else:
            print('Seu nome contém espaços.')

        print(f'Existem {size} caracteres no seu nome')
        break

    else:
        print('Desculpe, você deixou campos vazios')
