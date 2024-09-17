from robo import Robo
from robo_medico import RoboMedico
from robo_lutador import RoboLutador
import random

# Instanciando alguns robôs
robo1 = RoboLutador("Robo1")
robo2 = RoboLutador("Robo2")
medico = RoboMedico("Medico1")

print(robo1)
print(robo2)
print(medico)

# Luta entre robôs
robo1.atacar(robo2)

# Verificar se precisa de médico
if robo2.vida < 0.1 and random.choice([True, False]):
    print(f'{robo2.nome} chama o médico!')
    medico.curar(robo2)

# Reproduzir dois robôs
bebezinho = robo1 + robo2
print(f'Novo robô gerado: {bebezinho}')
