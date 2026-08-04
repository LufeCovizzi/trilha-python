# Manipulando Strings em Python
# Estudado em: 04/08/2026
# Curso: Manipulando Strings com Python - DIO/Luizalabs

# A lógica: strings em Python são "sequências indexadas", isso significa que cada caractere tem uma posição numerada, começando do zero.

nome = "Luiz Fernando"

# --- INDEXAÇÃO: acessar caracteres por posição ---
print(nome[0])    # 'L' -> primeira posição (índice 0)
print(nome[-1])   # 'o' -> índice negativo conta de trás pra frente

# --- SLICING: pegar um "pedaço" da string ---
print(nome[0:4])   # 'Luiz' -> da posição 0 até a 4 (sem incluir a 4)
print(nome[5:])    # 'Fernando' -> da posição 5 até o final

# --- MÉTODOS ÚTEIS DE STRING ---
print(nome.upper())        # 'LUIZ FERNANDO' -> tudo maiúsculo
print(nome.lower())        # 'luiz fernando' -> tudo minúsculo
print(nome.replace("Luiz", "João"))  # troca um trecho por outro
print(len(nome))           # 13 -> tamanho da string (quantidade de caracteres)
print(nome.split(" "))     # ['Luiz', 'Fernando'] -> quebra a string em uma lista

# --- F-STRINGS: a forma moderna de formatar texto ---
idade = 27
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos"
print(mensagem)

# Por que usar f-string em vez de concatenar com +?
# Compare:
mensagem_antiga = "Meu nome é " + nome + " e eu tenho " + str(idade) + " anos"
# A f-string é mais legível e evita ter que converter número pra string manualmente
# (repare que no jeito antigo precisei usar str(idade), na f-string não precisa)

# --- STRINGS SÃO IMUTÁVEIS ---
# Isso significa que você não pode alterar um caractere específico direto.
# nome[0] = "P"  -> isso daria ERRO (TypeError)
# O certo é criar uma string nova a partir da antiga, como fizemos com .replace()
