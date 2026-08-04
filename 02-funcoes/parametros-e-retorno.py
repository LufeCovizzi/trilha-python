# Parâmetros e Retorno em Python
# Estudado em: 04/08/2026
# Curso: Dominando Funções Python - DIO/Luizalabs

# --- FUNÇÃO COM RETURN ---
def somar(a, b):
    resultado = a + b
    return resultado

# A diferença crucial: como a função TEM return, dá pra guardar o resultado
soma_total = somar(5, 3)
print(soma_total)  # 8

# Se a função só tivesse print() em vez de return, "soma_total" seria None,
# porque você não estaria capturando nenhum valor de volta.

# --- COMPARANDO PRINT vs RETURN ---
def somar_com_print(a, b):
    print(a + b)  # só mostra na tela, não devolve nada

def somar_com_return(a, b):
    return a + b  # devolve o valor pra quem chamou

resultado_1 = somar_com_print(3, 4)   # imprime 7, mas resultado_1 = None
resultado_2 = somar_com_return(3, 4)  # não imprime nada sozinho, mas resultado_2 = 7

print(resultado_1)  # None
print(resultado_2)  # 7

# --- POR QUE ISSO IMPORTA NA PRÁTICA? ---
# Porque o resultado de uma função com return pode ser usado em outros cálculos:
def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

media_aluno = calcular_media(7, 8, 9)
if media_aluno >= 7:
    print(f"Aprovado com média {media_aluno}")
else:
    print(f"Reprovado com média {media_aluno}")

# Isso só é possível porque calcular_media() DEVOLVE um número,
# que pode ser comparado, somado, usado em outra função, etc.

# --- *ARGS: número variável de argumentos posicionais ---
# Útil quando você não sabe de antemão quantos valores vão ser passados
def somar_varios(*numeros):
    return sum(numeros)

print(somar_varios(1, 2, 3))        # 6
print(somar_varios(10, 20, 30, 40)) # 100

# --- **KWARGS: número variável de argumentos nomeados ---
def exibir_dados(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Luiz", idade=27, cidade="Mirassol")
# Isso é parecido com um dicionário sendo passado "solto" pra função
