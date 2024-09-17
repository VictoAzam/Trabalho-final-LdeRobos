from robo import Robo
import random

class RoboMedico(Robo):
    def __init__(self, nome: str):
        super().__init__(nome)
        self._poder_de_cura = random.uniform(0, 1)

    @property
    def poder_de_cura(self):
        return self._poder_de_cura

    def mensagem_cura(self):
        print("|-------------------------------|")
        print("|       + Voce foi curado +      |")
        print("|-------------------------------|")

    def curar(self, robo):
        if robo.vida < 1 and self.vida >= robo.vida:
            cura = min(1 - robo.vida, self.poder_de_cura)
            robo.vida += cura
            print(f'{self.nome} curou {robo.nome} em {cura:.2f} pontos de vida!')
            self.mensagem_cura()
        else:
            print(f'{self.nome} não conseguiu curar {robo.nome}.')
