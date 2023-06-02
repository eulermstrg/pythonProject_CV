while True:
    num_str = input("Digite um número inteiro: ")

# O bloco abaixo trata a exceção para números inteiros
    try:
        num_1 = int(num_str)
        break
    except ValueError:
        print("Não é um número inteiro válido.")

if num_1 % 2 == 0:
    print("Número par")
else:
    print("Número ímpar")
