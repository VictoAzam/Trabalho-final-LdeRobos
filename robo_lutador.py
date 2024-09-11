from robo import Robo
import random

class RoboLutador(Robo):
    dano_maximo = 0.2

    def __init__(self, nome: str):
        super().__init__(nome)
        self._poder = random.uniform(self.dano_maximo, 1)

    @property
    def poder(self):
        return self._poder

    def desenhar_estrela(self):
        print("  *  ")
        print(" * * ")
        print("*****")
        print(" * * ")
        print("  *  ")

    def desenhar_cruz(self):
        print("  *  ")
        print("  *  ")
        print("*****")
        print("  *  ")
        print("  *  ")

    def atacar(self, outro_robo):
        print(f'{self.nome} ataca {outro_robo.nome}!')
        self.desenhar_estrela()
        outro_robo.vida *= (1 - self.poder)
        print(f'{outro_robo.nome} agora tem {outro_robo.vida:.2f} de vida.')

        if isinstance(outro_robo, RoboLutador):
            print(f'{outro_robo.nome} contra-ataca {self.nome}!')
            self.desenhar_estrela()
            self.vida *= (1 - outro_robo.poder)
            print(f'{self.nome} agora tem {self.vida:.2f} de vida.')

        if outro_robo.vida <= 0:
            print(f'{outro_robo.nome} foi destruído!')
            self.desenhar_cruz()
