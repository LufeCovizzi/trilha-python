# Tuplas em Python
# Estudado em: 10/09/2026
# Curso: Conhecendo Tuplas em Python - DIO/Luizalabs

# --- CRIANDO UMA TUPLA ---
coordenada = (23.5505, -46.6333)  # latitude, longitude de São Paulo

print(coordenada[0])  # 23.5505
print(coordenada[1])  # -46.6333

# --- TUPLAS SÃO IMUTÁVEIS ---
# coordenada[0] = 10  -> isso daria ERRO (TypeError)
# Diferente da lista, não dá pra alterar um item depois de criada.

# --- QUANDO USAR TUPLA EM VEZ DE LISTA? ---
# Use tupla quando os dados representam algo que NÃO deveria mudar,
# como coordenadas geográficas, um RGB de cor (255, 0, 0), ou dias da semana.
# Use lista quando os dados VÃO mudar ao longo do programa (adicionar, remover, editar).

# --- DESEMPACOTAMENTO (unpacking) ---
# Um recurso bem útil de tupla: atribuir os valores direto a variáveis
latitude, longitude = coordenada
print(latitude)   # 23.5505
print(longitude)  # -46.6333

# --- TUPLA COM MÚLTIPLOS TIPOS ---
pessoa = ("Luiz", 27, "Mirassol")
nome, idade, cidade = pessoa
print(f"{nome} tem {idade} anos e mora em {cidade}")
