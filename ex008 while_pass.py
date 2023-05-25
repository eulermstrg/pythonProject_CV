import os

while True:
    senha = input(' Digite a senha: ')

    if senha != '123':
        print('Senha incorreta')
        # Limpar a tela
        os.system('cls' if os.name == 'nt' else 'clear')

    elif senha == '123':
        print('Senha correta, bem vindo!')
        break
