while True:
    hora_strg = input('Digite a hora atual: ')

    try:
        hora_int = int(hora_strg)

        if 0 <= hora_int <= 23:
            if 0 <= hora_int <= 11:
                print('Bom dia')
            elif 12 <= hora_int <= 17:
                print('Boa tarde')
            else:
                print('Boa noite')
            break
        else:
            print('Não é uma hora válida')
    except ValueError:
        print('Dão é uma hora válida')
