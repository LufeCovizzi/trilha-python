# Tipos de Operadores em Python
# Estudado em: 30/07/2026
# Curso: Tipos de Operadores com Python - DIO/Luizalabs

# --- OPERADORES ARITMÉTICOS ---
a = 10
b = 3

print(a + b)   # 13  → soma
print(a - b)   # 7   → subtração
print(a * b)   # 30  → multiplicação
print(a / b)   # 3.333... → divisão "real" (sempre retorna float)
print(a // b)  # 3   → divisão inteira (descarta a parte decimal)
print(a % b)   # 1   → módulo (resto da divisão)
print(a ** b)  # 1000 → potenciação (10 elevado a 3)

# Por que existe // separado de /?
# Às vezes você quer saber "quantas vezes cabe inteiro", não o valor exato.
# Exemplo prático: dividir 10 balas entre 3 pessoas -> cada uma recebe 10 // 3 = 3 balas,
# e sobram 10 % 3 = 1 bala.

# --- OPERADORES DE COMPARAÇÃO ---
# Sempre retornam um booleano (True ou False)
print(a == b)   # False → a é igual a b?
print(a != b)   # True  → a é diferente de b?
print(a > b)    # True  → a é maior que b?
print(a < b)    # False → a é menor que b?

# ARMADILHA COMUM: confundir = com ==
# x = 5   -> isso ATRIBUI o valor 5 à variável x
# x == 5  -> isso COMPARA se x é igual a 5, retorna True ou False
# Usar = onde deveria ser == é um dos erros mais comuns de iniciante.

# --- OPERADORES LÓGICOS ---
idade = 20
tem_carteira = True

print(idade >= 18 and tem_carteira)  # True → as DUAS condições precisam ser verdadeiras
print(idade >= 18 or tem_carteira)   # True → PELO MENOS UMA condição precisa ser verdadeira
print(not tem_carteira)              # False → inverte o valor booleano

# Uso prático: verificar se alguém pode dirigir
pode_dirigir = idade >= 18 and tem_carteira
print(pode_dirigir)  # True

# --- OPERADORES DE ATRIBUIÇÃO ---
contador = 0
contador += 1   # equivale a: contador = contador + 1
print(contador)  # 1

contador *= 5   # equivale a: contador = contador * 5
print(contador)  # 5

# Por que usar += em vez de escrever tudo? É mais curto e é o padrão usado
# em loops para "acumular" um valor a cada repetição (você vai ver isso na Aula 3).
