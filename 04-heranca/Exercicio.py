# Exercício: Hierarquia de Equipamentos de Laboratório

# O cenário: você vai modelar equipamentos de laboratório usando herança, parecido com o que pode aparecer no LabTrack no futuro.

# Passo 1 — Classe base

# Crie uma classe EquipamentoLab com:

# __init__ recebendo nome e codigo_patrimonio
# Um método exibir_info() que imprime algo como "Equipamento: {nome} | Patrimônio: {codigo_patrimonio}"

class EquipamentoLab:
    def __init__(self, nome, codigo_patrimonio):
        self.nome = nome
        self.codigo_patrimonio = codigo_patrimonio
        
    def exibir_info(self):
        print(f"Equipamento: {self.nome} | Patrimônio: {self.codigo_patrimonio}")

# Passo 2 — Duas classes filhas com herança simples

# Crie Centrifuga e Microscopio, ambas herdando de EquipamentoLab:

# Centrifuga precisa de um atributo extra: rpm_maximo (velocidade máxima de rotação). Por causa disso, ela vai precisar sobrescrever o __init__ e usar super() (igual fizemos com Caminhao)
# Microscopio precisa de um atributo extra: aumento_maximo (ex: “1000x”). Mesma lógica: __init__ próprio com super()

# Cada uma dessas duas classes também deve ter um método específico:

# Centrifuga → um método centrifugar(tempo_minutos) que imprime algo como "Centrifugando por {tempo_minutos} minutos a {rpm_maximo} RPM"
# Microscopio → um método focar() que imprime "Focando imagem com aumento de {aumento_maximo}"

class Centrifuga(EquipamentoLab):
    def __init__(self, nome, codigo_patrimonio, rpm_maximo):
        super().__init__(nome, codigo_patrimonio)
        self.rpm_maximo = rpm_maximo

    def centrifugar(self, tempo_minutos):
        print(f"Centrifugando por {tempo_minutos} minutos a {self.rpm_maximo} RPM")
    

class Microscopio(EquipamentoLab):
    def __init__(self, nome, codigo_patrimonio, aumento_maximo):
        super().__init__(nome, codigo_patrimonio)
        self.aumento_maximo = aumento_maximo

    
    def focar(self):
        print (f"Focando a imagem com aumento de {self.aumento_maximo}")

# Passo 3 — Testando

# Crie um objeto de cada classe, chame exibir_info() (herdado) e o método específico de cada uma.

microscopio = Microscopio("Microscopio 1", "2002b", "1000x")
microscopio.exibir_info()  # herdado de EquipamentoLab
microscopio.focar()         # método específico do Microscopio

centrifuga = Centrifuga("Centrifuga 1", "Patrimônio 2003b", "12000")
centrifuga.exibir_info()
centrifuga.centrifugar(10)