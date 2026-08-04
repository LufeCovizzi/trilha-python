# Funções Básicas em Python
# Estudado em: 04/08/2026
# Curso: Dominando Funções Python - DIO/Luizalabs

# --- FUNÇÃO SEM PARÂMETRO ---
def saudacao():
    print("Olá! Bem-vindo ao estudo de funções.")

saudacao()  # isso "chama" a função, executando o que está dentro dela
saudacao()  # pode chamar quantas vezes quiser

# --- FUNÇÃO COM PARÂMETRO ---
# Parâmetro = uma "entrada" que a função espera receber
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Bem-vindo.")

saudacao_personalizada("Luiz")
saudacao_personalizada("Maria")

# Por que isso é útil? A MESMA função funciona pra qualquer nome,
# em vez de escrever um print() diferente pra cada pessoa.

# --- FUNÇÃO COM MÚLTIPLOS PARÂMETROS ---
def apresentar(nome, idade, cidade):
    print(f"{nome} tem {idade} anos e mora em {cidade}")

apresentar("Luiz", 27, "Mirassol")

# --- PARÂMETROS COM VALOR PADRÃO (default) ---
# Se quem chamar a função não informar esse parâmetro, ele usa o valor padrão
def saudacao_idioma(nome, idioma="português"):
    if idioma == "português":
        print(f"Olá, {nome}!")
    elif idioma == "inglês":
        print(f"Hello, {nome}!")

saudacao_idioma("Luiz")              # usa o padrão "português"
saudacao_idioma("Luiz", "inglês")    # sobrescreve o padrão

# --- CHAMANDO POR NOME DO PARÂMETRO (keyword arguments) ---
# Isso deixa a chamada mais clara, principalmente com muitos parâmetros
apresentar(nome="Luiz", cidade="Mirassol", idade=27)
# Repare que a ORDEM não importa aqui, porque estamos nomeando cada parâmetro
