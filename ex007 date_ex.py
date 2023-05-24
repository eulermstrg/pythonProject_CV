def subtrair_horarios(horario1, horario2):
    # Separando as partes do primeiro horário
    h1, m1, s1 = map(int, horario1.split(':'))

    # Separando as partes do segundo horário
    h2, m2, s2 = map(int, horario2.split(':'))

    # Convertendo os horários para segundos
    total_segundos1 = h1 * 3600 + m1 * 60 + s1
    total_segundos2 = h2 * 3600 + m2 * 60 + s2

    # Subtraindo os horários
    diferenca_segundos = total_segundos2 - total_segundos1

    # Convertendo a diferença de volta para o formato "hh:mm:ss"
    horas = diferenca_segundos // 3600
    minutos = (diferenca_segundos % 3600) // 60
    segundos = diferenca_segundos % 60

    # Retornando a diferença formatada
    diferenca_formatada = f'{horas:02}:{minutos:02}:{segundos:02}'
    return diferenca_formatada


# Exemplo de uso
horario1 = input("Digite o primeiro horário (hh:mm:ss): ")
horario2 = input("Digite o segundo horário (hh:mm:ss): ")

diferenca = subtrair_horarios(horario1, horario2)
print("A diferença entre os horários é:", diferenca)
