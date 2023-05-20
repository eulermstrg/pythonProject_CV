while True:
    entrada = input("Digite um valor: ")

    try:
        # Tentar converter o input para diferentes tipos primitivos e salvar em variáveis
        texto = str(entrada)
        inteiro = int(entrada)
        flutuante = float(entrada)
        booleano = bool(entrada)

        # Exibir apenas as variáveis convertidas com sucesso
        print("Valores convertidos com sucesso:")
        if texto:
            print("Valor como texto:", texto)
        if isinstance(inteiro, int):
            print("Valor como inteiro:", inteiro)
        if isinstance(flutuante, float):
            print("Valor como flutuante:", flutuante)
        if isinstance(booleano, bool):
            print("Valor como booleano:", booleano)

        break  # Sai do loop se não houver erro

    except ValueError:
        print("Entrada inválida! Certifique-se de inserir um valor numérico válido.\n")
    except TypeError:
        print("Entrada inválida! Não é possível converter para um tipo primitivo.\n")
