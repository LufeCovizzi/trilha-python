# Listas em Python
# Estudado em: [preencha a data]
# Curso: Trabalhando com Listas em Python - DIO/Luizalabs

# --- CRIANDO E ACESSANDO ---
linguagens = ["Python", "JavaScript", "HTML", "CSS"]

print(linguagens[0])   # 'Python'
print(linguagens[-1])  # 'CSS' -> último item

# --- LISTAS SÃO MUTÁVEIS (diferente de string!) ---
linguagens[1] = "TypeScript"  # isso funciona, strings não permitiriam
print(linguagens)  # ['Python', 'TypeScript', 'HTML', 'CSS']

# --- MÉTODOS ÚTEIS ---
linguagens.append("SQL")        # adiciona no final
print(linguagens)

linguagens.remove("HTML")       # remove pelo valor
print(linguagens)

linguagens.insert(0, "Git")     # insere numa posição específica
print(linguagens)

print(len(linguagens))          # quantidade de itens
print("Python" in linguagens)   # True -> verifica se um item existe na lista

# --- PERCORRENDO UMA LISTA (usando o for que já vimos) ---
for linguagem in linguagens:
    print(f"Estudando: {linguagem}")

# --- LIST COMPREHENSION (forma compacta de criar listas) ---
# Isso é um pouco mais avançado, mas vale conhecer:
numeros = [1, 2, 3, 4, 5]
dobrados = [n * 2 for n in numeros]
print(dobrados)  # [2, 4, 6, 8, 10]

# Isso é equivalente a escrever:
dobrados_v2 = []
for n in numeros:
    dobrados_v2.append(n * 2)
# Só que em uma linha só - útil quando o loop é simples
