# Polimorfismo em Python (POO)
# Estudado em: 16/10/26
# Curso: Conhecendo Polimorfismo em Python - DIO

# --- O QUE É POLIMORFISMO? ---
# A palavra vem do grego: "poli" (muitas) + "morfo" (formas) = "muitas formas".
# Na prática, significa que o MESMO nome de método pode ter comportamentos
# DIFERENTES dependendo de qual objeto está chamando ele.
#
# Você já usou isso sem perceber: o operador + funciona diferente dependendo
# do tipo dos operandos - soma números, mas concatena strings.

print(2 + 3)        # 5          -> soma numérica
print("a" + "b")    # "ab"       -> concatenação de texto

# O "+" é o mesmo símbolo, mas o COMPORTAMENTO muda de acordo com o tipo.
# Polimorfismo em classes funciona com essa mesma ideia, aplicada a métodos.

# --- POLIMORFISMO SEM HERANÇA: classes sem relação nenhuma, mesmo método ---
class Pardal:
    def voar(self):
        print("Pardal pode voar")

class Aviao:
    def voar(self):
        print("Avião está decolando...")

# Repare: Pardal e Aviao NÃO têm relação de herança nenhuma entre si.
# Mas as duas têm um método chamado "voar()", cada uma com sua própria lógica.

def executar_voo(objeto):
    objeto.voar()  # chama "voar()" seja lá de qual classe o objeto for

executar_voo(Pardal())  # "Pardal pode voar"
executar_voo(Aviao())   # "Avião está decolando..."

# A função executar_voo() NÃO PRECISA SABER qual classe está recebendo -
# ela só confia que, seja lá o que for, aquele objeto tem um método voar().
# Isso é a essência do polimorfismo: tratar objetos diferentes de forma
# uniforme, desde que eles "respondam" ao mesmo método.

# --- POR QUE ISSO IMPORTA? ---
# Sem polimorfismo, você precisaria escrever um "if" pra cada tipo de objeto:
#
# def executar_voo_sem_polimorfismo(objeto):
#     if isinstance(objeto, Pardal):
#         print("Pardal pode voar")
#     elif isinstance(objeto, Aviao):
#         print("Avião está decolando...")
#
# Fica óbvio que isso não escala: a cada novo tipo de "coisa que voa" que
# você criar, teria que voltar nessa função e adicionar mais um elif.
# Com polimorfismo, a função nem precisa mudar - só a nova classe precisa
# ter o método voar() implementado.