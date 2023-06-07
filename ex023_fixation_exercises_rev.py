# # Exercícios de fixação
#
# # Receba um nome e faça um loop para exibir apenas uma letra de cada vez
#
# nome = input('Digite um nome: ')
# i = 1
#
# # for letra in nome:
# #     print(letra)
#
# # Use o nome do código acima para exibir a posição da letra no nome, junto com a letra.

nome = input('Digite um nome: ')

for i, letra in enumerate(nome, start=1):
    print(f'A {i}ª letra é {letra}')

