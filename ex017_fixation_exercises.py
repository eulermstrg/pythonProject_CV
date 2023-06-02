while True:
    nome = input('Digite seu nome: ')

    if nome.isnumeric():
        print('Não é um nome, informe um nome por gentileza')
    else:
        qtd_letras = len(nome)
        if qtd_letras <= 4:
            print('Nome pequeno')
        elif qtd_letras <= 6:
            print('Nome normal')
        else:
            print('Nome grande')
        print(f'Seu nome tem {qtd_letras} letras')
        break
