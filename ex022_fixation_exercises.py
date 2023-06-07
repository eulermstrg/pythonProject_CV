from datetime import datetime


def data_por_extenso(data):
    try:
        # Verifica se a data está no formato correto
        datetime.strptime(data, "%d/%m/%Y")

        # Extrai o dia, mês e ano da data fornecida
        dia, mes, ano = map(int, data.split('/'))

        # Lista com os meses por extenso
        meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
                 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

        # Monta a string com a data por extenso
        data_extenso = f"{dia} de {meses[mes - 1]} de {ano}"

        return data_extenso

    except ValueError:
        # Data inválida
        return None


data = input("Digite uma data no formato DD/MM/AAAA: ")
data_extenso = data_por_extenso(data)

if data_extenso is not None:
    print(data_extenso)
else:
    print("Data inválida!")
