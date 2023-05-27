numero_str = input('Digite um número: ')

try:
    print(f'"{numero_str}"')
    numero_float = float(numero_str)
    print('Float:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:
    print(f'"{numero_str}" não é um número!')
