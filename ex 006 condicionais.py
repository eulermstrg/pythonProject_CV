while True:
    entrada = input('[e] para entrar e  [s] para sair: ')

    if entrada == 'e' or entrada == 'E':
        senha = int(input('digite a senha: '))

        if senha == 123:
            print('entrada realizada')
            break
        else:
            print('senha errada, favor verificar')

    elif entrada == 's' or entrada == 'S':
        print('obrigado por usar os serviços.')
        break
    else:
        print('Digite uma opção válida!')
