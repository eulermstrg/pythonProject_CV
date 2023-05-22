class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")


# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("João", 25)

# Chamando o método saudacao da instância
pessoa1.saudacao()
