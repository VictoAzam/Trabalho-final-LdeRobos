from robo import Robo
from robo_medico import RoboMedico
from robo_lutador import RoboLutador
import random

#  alguns robôs
robo1 = RoboLutador("rodoberto lutador")
robo2 = RoboLutador("Godoberto lutador")
medico = RoboMedico("Dr Lodoberto")

print(robo1)
print(robo2)
print(medico)

def rodada_ataque(atacante, defensor):
    """Simula o ataque de um robô a outro."""
    print(f'{atacante.nome} ataca {defensor.nome}')
    atacante.atacar(defensor)

def chamar_medico(robo, medico):
    """Chance de chamar o médico se a vida do robô estiver baixa."""
    if robo.vida < 0.1 and random.choice([True, False]):
        print(f'{robo.nome} chama o médico!')
        medico.curar(robo)

def jogo_terminado(robo1, robo2):
    """Verifica se o jogo terminou (um dos robôs com vida <= 0)."""
    return robo1.vida <= 0 or robo2.vida <= 0

# Número de rounds
rounds = 5

for round_num in range(1, rounds + 1):
    print(f'\n--- Round {round_num} ---')

    rodada_ataque(robo1, robo2)

    if jogo_terminado(robo1, robo2):
        break

    rodada_ataque(robo2, robo1)

    if jogo_terminado(robo1, robo2):
        break

    chamar_medico(robo2, medico)

    chamar_medico(robo1, medico)

# Verificar qual robô venceu
if robo1.vida > 0 and robo2.vida <= 0:
    print(f'{robo1.nome} venceu!')
elif robo2.vida > 0 and robo1.vida <= 0:
    print(f'{robo2.nome} venceu!')
else:
    print('O jogo terminou em empate!')

if robo1.vida > 0 and robo2.vida > 0:
    bebezinho = robo1 + robo2
    print(f'Novo robô gerado: {bebezinho}')
