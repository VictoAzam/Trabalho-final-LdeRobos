

# 🦾 Luta de Robôs em Python

Atividade Trabalo Final Professor  HABIB ASSEISS NETO
Este é um projeto em Python que simula lutas entre robôs utilizando os conceitos de **Orientação a Objetos**. O projeto inclui diferentes tipos de robôs, como robôs lutadores e médicos, que podem atacar, se curar e até se reproduzirem! Além disso, as batalhas e eventos (como curas e destruições) são acompanhados de representações visuais em ASCII.

## 🚀 Funcionalidades

- **Luta entre Robôs**: Robôs lutadores podem atacar outros robôs, reduzindo suas vidas de acordo com o poder de ataque.
- **Cura de Robôs**: Robôs médicos podem curar robôs que estão gravemente feridos.
- **Reprodução de Robôs**: Dois robôs podem se reproduzir e gerar um novo robô com o nome combinado dos pais.
- **Representações Visuais**: Eventos importantes como ataques, curas e destruições são representados com gráficos ASCII no terminal.
  - Ataque: Desenha uma estrela de 5 pontas.
  - Morte: Desenha uma cruz.
  - Cura: Apresenta uma mensagem especial.
  - Reprodução: Exibe um robô "bebê" em ASCII.

## 🛠️ Estrutura do Projeto

O projeto está organizado em diferentes arquivos Python, cada um representando uma classe específica:

- `robo.py`: Classe base **Robo**, define os atributos e comportamentos comuns a todos os robôs.
- `robo_lutador.py`: Subclasse **RoboLutador**, especializada em combate, com poder de ataque e contra-ataque.
- `robo_medico.py`: Subclasse **RoboMedico**, especializada em curar outros robôs.
- `main.py`: Script principal para executar simulações de lutas, curas e reproduções entre os robôs.

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/luta-de-robos.git
   cd luta-de-robos
   ```

2. Certifique-se de ter o Python instalado (Python 3.6 ou superior).
3. Execute o arquivo `main.py` para rodar o projeto:

   ```bash
   python main.py
   ```

## 📄 Como Funciona

### Robôs Lutadores
- **Atributo de classe `dano_maximo`**: Define o dano máximo que um robô lutador pode causar.
- **Método `atacar()`**: Permite que o robô ataque outro robô, reduzindo sua vida.
- Se o robô atacado for também um robô lutador, ele contra-ataca.

### Robôs Médicos
- **Atributo `poder_de_cura`**: Define a quantidade de cura que o robô médico pode fornecer.
- **Método `curar()`**: Cura outro robô se sua vida estiver baixa e a do médico for suficiente.

### Reprodução
- Dois robôs podem se reproduzir usando a sobrecarga do operador `+`, gerando um novo robô com o nome formado pelos nomes dos pais.

## 🎮 Exemplo de Uso

Aqui está um exemplo de como o jogo pode ser usado:

```python
from robo import Robo
from robo_lutador import RoboLutador
from robo_medico import RoboMedico

# Instanciação dos robôs
lutador1 = RoboLutador("Lutador1")
lutador2 = RoboLutador("Lutador2")
medico = RoboMedico("Medico")

# Luta entre dois robôs lutadores
lutador1.atacar(lutador2)

# Médico cura o lutador ferido
if lutador2.vida < 0.1:
    medico.curar(lutador2)

# Reprodução entre os robôs lutadores
bebezinho = lutador1 + lutador2
```

## 📚 Requisitos

- **Python 3.6 ou superior**
- Bibliotecas padrão do Python (`random`)

## 📝 Contribuição

Se você deseja contribuir com o projeto, siga os seguintes passos:

1. Fork o projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-feature`).
3. Faça o commit de suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

