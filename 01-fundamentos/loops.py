# Loops em Python
# Estudado em: 01/08/26
# Curso: Estruturas Condicionais e de Repetição em Python - DIO/Luizalabs

# --- FOR: quando sabemos a quantidade ---
for i in range(5):
    print(i)  # imprime 0, 1, 2, 3, 4 (range vai até 5, mas NÃO inclui o 5)

# Por que começa em 0? Convenção da linguagem (quase toda linguagem de programação
# começa contagem em 0, não em 1) - vale se acostumar com isso desde já.

# FOR percorrendo uma lista diretamente
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# --- WHILE: quando depende de uma condição ---
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # ESSENCIAL: sem isso, o loop nunca termina (loop infinito)

# ARMADILHA COMUM: esquecer de atualizar a variável de controle dentro do while
# Isso trava o programa - ele fica preso repetindo pra sempre.

# --- BREAK e CONTINUE ---
# break: interrompe o loop imediatamente
for numero in range(10):
    if numero == 5:
        break  # para assim que numero chega a 5
    print(numero)  # imprime 0, 1, 2, 3, 4

# continue: pula pra próxima repetição, sem executar o resto do bloco
for numero in range(5):
    if numero == 2:
        continue  # pula o print quando numero for 2
    print(numero)  # imprime 0, 1, 3, 4 (o 2 é pulado)
