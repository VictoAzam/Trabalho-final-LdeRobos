import random

class Robo:
    nivel_critico = 0.60

    def __init__(self, nome: str):
        self._nome = nome.split('-')[0]  
        self._vida = random.uniform(0, 1)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.split('-')[0]  #Nome Padrao

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        # Garante que a vida esteja entre 0 e 1
        self._vida = max(0, min(1, valor))

    def __repr__(self):
        return f'Robo({self.nome}, vida={self.vida:.2f})'

    def __add__(self, outro_robo):
        novo_nome = f'{self.nome}-{outro_robo.nome}'
        robozinho = self.desenhar_robozinho()
        print(f'{self.nome} e {outro_robo.nome} se reproduziram! Aqui está o novo robô:')
        print(robozinho)
        return type(self)(novo_nome)

    def precisa_de_medico(self):
        return self.vida < self.nivel_critico

    def desenhar_robozinho(self):
        return """
      \_/      
     (* *)     
    __)#(__    
   ( )...( )  (_)
   || |_| ||  // 
>==() | | () /  
    _(___)_    
   [-]   [-]Robo
"""
