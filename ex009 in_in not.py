while True:
    nome = input('Digite seu nome: ')

    encontrar = input('Digite o trecho que deseja procurar no nome: ')

    if encontrar in nome:
        print('{} está em {}'.format(encontrar, nome))
        break
    else:
        print('{} não está em {}, vamos tentar outra vez!'.format(encontrar, nome))
