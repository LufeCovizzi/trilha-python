# Estruturas Condicionais em Python
# Estudado em: 30/07/2026
# Curso: Estruturas Condicionais e de Repetição em Python - DIO/Luizalabs

idade = 16

# --- IF simples ---
if idade >= 18:
    print("Maior de idade")

# --- IF / ELSE ---
if idade >= 18:
    print("Pode votar")
else:
    print("Não pode votar")

# --- IF / ELIF / ELSE ---
# elif = "senão, se" -> permite testar várias condições em sequência
nota = 7.5

if nota >= 9:
    print("Conceito A")
elif nota >= 7:
    print("Conceito B")
elif nota >= 5:
    print("Conceito C")
else:
    print("Reprovado")

# Por que a ORDEM do elif importa?
# O Python testa de cima pra baixo e para na PRIMEIRA condição verdadeira.
# Se nota = 9.5, ele já entra no primeiro "if nota >= 9" e nem olha os outros.

# --- CONDICIONAIS ANINHADAS (uma dentro da outra) ---
usuario_logado = True
eh_admin = False

if usuario_logado:
    if eh_admin:
        print("Bem-vindo, administrador")
    else:
        print("Bem-vindo, usuário comum")
else:
    print("Faça login primeiro")

# Isso poderia ser reescrito com "and", mais legível às vezes:
if usuario_logado and eh_admin:
    print("Acesso total")
