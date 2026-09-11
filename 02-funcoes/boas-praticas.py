# Boas Práticas com Funções em Python
# Estudado em: 10/09/2026
# Curso: Dominando Funções Python - DIO/Luizalabs

# --- PRINCÍPIO 1: uma função deve fazer UMA coisa só ---

# Ruim: essa função faz coisas demais ao mesmo tempo
def processar_pedido_ruim(nome, valor):
    print(f"Processando pedido de {nome}")
    imposto = valor * 0.1
    valor_final = valor + imposto
    print(f"Valor final: {valor_final}")
    return valor_final

# Melhor: quebrar em funções menores, cada uma com uma responsabilidade
def calcular_imposto(valor):
    return valor * 0.1

def calcular_valor_final(valor):
    return valor + calcular_imposto(valor)

def processar_pedido(nome, valor):
    valor_final = calcular_valor_final(valor)
    print(f"Pedido de {nome} processado. Valor final: {valor_final}")
    return valor_final

# Por que isso é melhor? Se amanhã o imposto mudar de 10% pra 12%,
# você só mexe em calcular_imposto() - sem precisar tocar no resto da lógica.
# Isso também facilita testar cada parte separadamente.

# --- PRINCÍPIO 2: nomes de função devem ser verbos que descrevem a ação ---
# Ruim: nome vago, não explica o que a função faz
def dados(x):
    return x * 2

# Melhor: nome descreve claramente a ação
def dobrar_valor(x):
    return x * 2

# --- PRINCÍPIO 3: evite "efeitos colaterais" escondidos ---
# Uma função que modifica algo fora dela sem deixar isso óbvio é perigosa

contador_global = 0

def incrementar_ruim():
    global contador_global  # modifica uma variável de fora da função
    contador_global += 1

# Isso funciona, mas é arriscado: quem lê "incrementar_ruim()" não sabe,
# só de olhar a chamada, que ela está alterando uma variável global.
# Prefira sempre que possível passar e retornar valores explicitamente:

def incrementar(valor):
    return valor + 1

contador = 0
contador = incrementar(contador)  # fica claro o que está acontecendo

# --- PRINCÍPIO 4: docstrings (documentação da função) ---
# Uma docstring explica o que a função faz, útil pra você e pra qualquer
# pessoa (ou recrutador!) que for ler seu código depois
def calcular_media(notas):
    """
    Calcula a média aritmética de uma lista de notas.

    Parâmetros:
        notas (list): lista de números representando as notas

    Retorna:
        float: a média das notas
    """
    return sum(notas) / len(notas)

print(calcular_media([7, 8, 9]))

# Dica: no VS Code, se você passar o mouse sobre uma função com docstring,
# ele mostra essa documentação automaticamente - é assim que bibliotecas
# profissionais (como o FastAPI que você está estudando) documentam suas funções.
