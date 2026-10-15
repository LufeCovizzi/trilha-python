# Herança em Python (POO)
# Estudado em: 15/10/26
# Curso: Aprendendo o Conceito de Herança com Python - DIO

# --- HERANÇA SIMPLES: a classe filha herda tudo da classe mãe ---
class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

# O (Veiculo) entre parênteses é o que declara a herança
class Motocicleta(Veiculo):
    pass  # "pass" = não precisa adicionar nada, já herda __init__ e ligar_motor

class Carro(Veiculo):
    pass

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()   # "Ligando o motor" -> veio de Veiculo, Motocicleta nunca escreveu isso
print(moto.cor)       # "preta" -> os atributos também vieram de Veiculo

# --- SOBRESCREVENDO O __init__ (quando a classe filha precisa de algo A MAIS) ---
# Caminhao precisa de um atributo extra que Veiculo não tem: "carregado".
# Por isso ela não pode só dar "pass" - ela precisa do PRÓPRIO __init__.
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        # super() chama o __init__ da classe MÃE (Veiculo), reaproveitando a lógica
        # que já existe lá, em vez de repetir "self.cor = cor" etc. de novo aqui.
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado  # esse atributo é exclusivo de Caminhao

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

caminhao = Caminhao("branco", "xde-0098", 4, True)
caminhao.ligar_motor()       # herdado de Veiculo, mesmo sem reescrever
caminhao.esta_carregado()    # método próprio de Caminhao
print(caminhao.cor)          # "branco" -> veio do super().__init__()

# --- POR QUE USAR super() EM VEZ DE REPETIR O CÓDIGO? ---
# Poderíamos ter escrito, dentro de Caminhao:
#   self.cor = cor
#   self.placa = placa
#   self.numero_rodas = numero_rodas
#   self.carregado = carregado
# Mas isso duplicaria a lógica que já existe em Veiculo.__init__().
# Se amanhã Veiculo ganhar um novo atributo (ex: "ano"), só precisamos mudar
# em UM lugar (Veiculo), e Caminhao recebe isso automaticamente via super().
# É o mesmo princípio de "evitar repetição" que vimos lá nas boas práticas de funções.

# --- DIFERENÇA ENTRE HERANÇA SIMPLES E HERANÇA MÚLTIPLA ---
# Simples: uma classe filha herda de UMA classe mãe só (tudo que vimos acima)
# Múltipla: uma classe filha herda de MAIS DE UMA classe mãe ao mesmo tempo

class Flutuante:
    def flutuar(self):
        print("Flutuando na água")

# Barco herda tanto de Veiculo quanto de Flutuante - combina os dois comportamentos
class Barco(Veiculo, Flutuante):
    pass

barco = Barco("azul", "brc-0001", 0)
barco.ligar_motor()  # veio de Veiculo
barco.flutuar()       # veio de Flutuante

# --- POR QUE ISSO IMPORTA PRA VOCÊ ESPECIFICAMENTE ---
# No LabTrack, se um dia você tiver "Amostra" e "Reagente" como tipos diferentes
# de item de laboratório, ambos compartilhando campos como data_cadastro e
# codigo_identificacao, herança evita repetir esses campos em cada classe -
# você cria uma classe base "ItemLaboratorio" e as duas herdam dela.