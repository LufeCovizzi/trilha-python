# Polimorfismo com Herança em Python (POO)
# Estudado em: 16/10/26
# Curso: Conhecendo Polimorfismo em Python - DIO

# --- A LÓGICA: combinar herança com polimorfismo ---
# Na herança (que você já estudou), a classe filha herda os métodos da
# classe pai. Mas é possível SOBRESCREVER um método herdado, dando a ele
# um comportamento diferente na classe filha - isso é particularmente útil
# quando o método herdado não se encaixa perfeitamente em todas as filhas.

class Passaro:
    def voar(self):
        print("Pássaro genérico voando")

# Pardal HERDA voar(), mas SOBRESCREVE com seu próprio comportamento
class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

# Avestruz também herda de Passaro, mas sobrescreve de um jeito diferente -
# porque biologicamente, um avestruz NÃO VOA, então faria sentido reescrever
# esse método em vez de usar o comportamento genérico herdado
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# --- SOBRESCRITA (OVERRIDE): o nome técnico desse comportamento ---
# Quando uma classe filha define um método com o MESMO NOME de um método já
# existente na classe pai, ela está "sobrescrevendo" (fazendo override)
# daquele método - o Python usa a versão da classe filha, não a da pai.

pardal = Pardal()
pardal.voar()     # "Pardal pode voar" -> usa a versão sobrescrita, não a genérica

avestruz = Avestruz()
avestruz.voar()   # "Avestruz não pode voar" -> versão própria, diferente do pardal

# --- POLIMORFISMO EM AÇÃO: tratando objetos diferentes de forma uniforme ---
def plano_voo(obj):
    obj.voar()  # não importa qual classe, só chama voar() e confia no resultado

plano_voo(Pardal())    # "Pardal pode voar"
plano_voo(Avestruz())  # "Avestruz não pode voar"

# A função plano_voo() trata Pardal e Avestruz da MESMA FORMA (chamando
# .voar()), mas cada um responde de um jeito diferente - isso é polimorfismo
# combinado com herança: mesmo "parentesco" (ambos são Passaro), comportamento
# diferente quando chamado.

# --- CUIDADO: usar herança só para "forçar" um método que não se encaixa ---
# Exemplo de uso questionável de herança/polimorfismo:
class Aviao(Passaro):  # FIXME: um Avião não é biologicamente um Pássaro!
    def voar(self):
        print("Avião está decolando...")

plano_voo(Aviao())  # funciona tecnicamente, mas semanticamente estranho

# Isso FUNCIONA no código (Python não vai reclamar), mas é um sinal de design
# ruim: herança deveria representar uma relação real de "é um tipo de"
# (Avestruz "é um tipo de" Passaro faz sentido biologicamente; Aviao "é um
# tipo de" Passaro, não). Quando você usa herança só pra "pegar emprestado"
# um método, sem a relação fazer sentido de verdade, geralmente existe um
# jeito melhor de resolver (como usar composição, assunto pra outra aula).

# --- POR QUE ISSO IMPORTA PRA VOCÊ ESPECIFICAMENTE ---
# No LabTrack, imagine uma classe base MetodoAnalise com um método
# executar(). Diferentes tipos de análise (PCR, SequenciamentoSanger,
# RTqPCR) poderiam herdar dela e sobrescrever executar() com a lógica
# específica de cada técnica - um serviço que roda análises não precisaria
# saber QUAL técnica está sendo usada, só chamaria .executar() e confiaria
# no polimorfismo pra rodar a versão certa.