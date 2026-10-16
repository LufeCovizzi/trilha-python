# Herança Múltipla e **kwargs em Python (POO)
# Estudado em: 15/10/26
# Curso: Aprendendo o Conceito de Herança com Python - DIO

# --- RELEMBRANDO: herança múltipla é quando uma classe filha herda de MAIS DE UMA classe mãe ---
# O problema que vamos resolver aqui: imagine Mamifero e Ave, duas classes com
# atributos DIFERENTES. Um Ornitorrinco é um caso raro na natureza que tem
# características de AMBOS ao mesmo tempo - por isso é um ótimo exemplo prático.

class Animal:
    def __init__(self, **kw):
        # **kw vai ser explicado logo abaixo - por enquanto, repare que o __init__
        # da classe mais "base" de todas não define atributo nenhum ainda.
        super().__init__(**kw)

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

# --- A HERANÇA MÚLTIPLA EM SI ---
# Ornitorrinco herda de DUAS classes ao mesmo tempo: Mamifero E Ave
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, nro_patas, **kw):
        self.nro_patas = nro_patas
        super().__init__(**kw)

# --- POR QUE **kwargs (kw) É NECESSÁRIO AQUI? ---
# Se cada classe recebesse só os parâmetros que ela mesma usa, dando super()
# com argumentos fixos, o Python teria dificuldade de "repassar" pra frente
# os parâmetros que uma classe não usa, mas a próxima da cadeia de herança usa.
#
# **kw funciona como um "pacote" que carrega TODOS os argumentos que sobraram
# e ainda não foram usados, repassando-os adiante pra próxima classe da cadeia
# via super().__init__(**kw) - até que cada um seja "capturado" pela classe
# que realmente precisa dele.

ornitorrinco = Ornitorrinco(
    nro_patas=4,
    cor_pelo="marrom",
    cor_bico="laranja"
)

print(ornitorrinco.nro_patas)  # 4       -> veio de Ornitorrinco
print(ornitorrinco.cor_pelo)   # marrom  -> veio de Mamifero
print(ornitorrinco.cor_bico)   # laranja -> veio de Ave

# Repare: cada atributo "nasceu" numa classe diferente da cadeia de herança,
# e o objeto final (ornitorrinco) tem acesso a todos eles.

# --- MRO: a ordem em que o Python procura os métodos (Method Resolution Order) ---
# Quando você escreve "class Ornitorrinco(Mamifero, Ave)", o Python monta uma
# ordem de busca: primeiro procura em Ornitorrinco, depois em Mamifero,
# depois em Ave, depois em Animal. Isso importa quando duas classes mãe têm
# um método/atributo com o MESMO nome - quem vem PRIMEIRO na herança "ganha".
print(Ornitorrinco.__mro__)
# Mostra a ordem exata que o Python usa para resolver cada chamada

