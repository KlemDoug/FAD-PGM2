# Arquivo de apoio ao Main.py com as classes que são importadas.
# Classe herdada Entrevistado.
class Entrevistado:
    def __init__(self, idade, genero):
        self.idade = idade
        self.genero = genero


# Classe herdeira Questoes.
class Questoes(Entrevistado):
    def __init__(self, idade, genero, q1, q2, q3, q4, dataehora):
        super().__init__(idade, genero)
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.dataehora = dataehora

