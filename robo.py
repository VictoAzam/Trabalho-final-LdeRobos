import random

class Robo:
    nivel_critico = 0.60

    def __init__(self, nome: str):
        self.nome = nome.split('-')[0]  # Considera só a primeira parte do nome
        self.vida = random.uniform(0, 1)

    def __repr__(self):
        return f'Robo({self.nome}, vida={self.vida:.2f})'

    def __add__(self, outro_robo):
        novo_nome = f'{self.nome}-{outro_robo.nome}'
        return type(self)(novo_nome)  # Cria o filho do mesmo tipo dos pais

    def precisa_de_medico(self):
        return self.vida < self.nivel_critico
