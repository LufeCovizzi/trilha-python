# Dicionários em Python
# Estudado em: 10/09/2026
# Curso: Aprendendo a Utilizar Dicionários em Python - DIO/Luizalabs

# --- CRIANDO E ACESSANDO ---
pessoa = {
    "nome": "Luiz Fernando",
    "idade": 27,
    "cidade": "Mirassol"
}

print(pessoa["nome"])   # 'Luiz Fernando' -> acessa pela CHAVE, não por posição
print(pessoa["idade"])  # 27

# --- ADICIONANDO E ALTERANDO VALORES ---
pessoa["profissao"] = "Desenvolvedor em formação"  # adiciona uma chave nova
pessoa["idade"] = 28  # altera um valor existente
print(pessoa)

# --- MÉTODOS ÚTEIS ---
print(pessoa.keys())     # todas as chaves
print(pessoa.values())   # todos os valores
print(pessoa.items())    # pares chave-valor

# --- ACESSO SEGURO COM .get() ---
# Se você tentar acessar uma chave que não existe com [ ], dá ERRO (KeyError)
# print(pessoa["salario"])  -> isso quebraria o programa

# O .get() é mais seguro: retorna None (ou um valor padrão) em vez de quebrar
print(pessoa.get("salario"))                    # None
print(pessoa.get("salario", "não informado"))   # 'não informado'

# --- PERCORRENDO UM DICIONÁRIO ---
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# --- DICIONÁRIO DENTRO DE LISTA (bem comum na prática) ---
# Exemplo: uma lista de vagas, cada vaga é um dicionário
vagas = [
    {"empresa": "Luby", "cargo": "Estagiário Dev", "remoto": True},
    {"empresa": "Visagio", "cargo": "Estagiário Software", "remoto": True}
]

for vaga in vagas:
    print(f"{vaga['cargo']} na {vaga['empresa']}")

# --- POR QUE ISSO IMPORTA PRA VOCÊ ESPECIFICAMENTE ---
# Quando você trabalha com FastAPI (como no seu LabTrack), o corpo das
# requisições e respostas da API geralmente vem/vai como JSON - que em
# Python é manipulado exatamente como um dicionário. Entender dicionário
# bem agora facilita muito quando você for lidar com Pydantic models.
