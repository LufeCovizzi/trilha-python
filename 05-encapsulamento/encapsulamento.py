# Encapsulamento, Recursos Públicos/Privados e Properties em Python (POO)
# Estudado em: 16/10/26
# Curso: Aplicando Encapsulamento em Python - DIO

# --- O QUE É ENCAPSULAMENTO? ---
# É o princípio de "esconder" os detalhes internos de uma classe, controlando
# como o mundo de fora acessa e modifica seus dados. Em vez de deixar qualquer
# código externo mexer direto nos atributos, a classe expõe métodos
# controlados pra isso - protegendo contra alterações indevidas e mantendo a
# lógica de validação centralizada em um lugar só.

# --- RECURSOS PÚBLICOS (o padrão em Python) ---
class PessoaPublica:
    def __init__(self, nome, idade):
        self.nome = nome    # público: qualquer código de fora pode ler E alterar
        self.idade = idade

pessoa_publica = PessoaPublica("Luiz", 28)
print(pessoa_publica.nome)      # acesso direto funciona normalmente
pessoa_publica.idade = -50      # PROBLEMA: nada impede um valor absurdo como esse
print(pessoa_publica.idade)     # -50 -> o Python não reclama, mas faz sentido?

# --- RECURSOS PRIVADOS (convenção com underscore) ---
# Python não tem "private" de verdade como Java (com palavra-chave bloqueando
# acesso). Em vez disso, usa CONVENÇÃO: um underscore (_) no início do nome
# sinaliza "isso é interno da classe, não mexa de fora" - mas tecnicamente
# ainda é possível acessar (é um acordo de respeito entre programadores, não
# uma trava real do interpretador).
class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome                      # underscore = "uso interno"
        self._ano_nascimento = ano_nascimento   # underscore = "uso interno"

    def get_nome(self):
        return self._nome

    def get_idade(self):
        ano_atual = 2026
        return ano_atual - self._ano_nascimento

pessoa = Pessoa("Guilherme", 1994)
print(pessoa.get_nome())    # acesso controlado, via método
print(pessoa.get_idade())   # a lógica de calcular idade fica centralizada aqui

# Ainda é POSSÍVEL fazer pessoa._nome diretamente (Python não bloqueia),
# mas o underscore é um sinal claro pra quem lê o código: "não faça isso".

# --- O PROBLEMA DE USAR get_nome() E get_idade() ASSIM ---
# Funciona, mas obriga quem usa a classe a lembrar de chamar um método
# toda vez, em vez de simplesmente acessar como se fosse um atributo comum
# (pessoa.idade, por exemplo). Isso é mais verboso do que precisa ser.

# --- A SOLUÇÃO: @property ---
# @property permite que um MÉTODO seja acessado como se fosse um ATRIBUTO,
# sem parênteses - mantendo o encapsulamento (a lógica interna continua
# controlada), mas com a sintaxe limpa de acesso direto.
class PessoaComProperty:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        ano_atual = 2026
        return ano_atual - self._ano_nascimento

    @property
    def nome(self):
        return self._nome

pessoa_property = PessoaComProperty("Guilherme", 1994)

# Repare: SEM parênteses, mesmo sendo um método por baixo dos panos
print(pessoa_property.idade)   # 32 -> parece um atributo, mas é calculado na hora
print(pessoa_property.nome)    # "Guilherme"

# pessoa_property.idade()  -> isso daria ERRO, porque @property remove a
# necessidade (e a possibilidade) de chamar com parênteses

# --- POR QUE @property É MELHOR QUE get_idade() AQUI? ---
# 1. Sintaxe mais limpa: pessoa.idade em vez de pessoa.get_idade()
# 2. A idade é CALCULADA a cada acesso (sempre correta, baseada no ano atual),
#    em vez de guardada como um número fixo que poderia ficar desatualizado
# 3. Se um dia você precisar mudar a lógica de cálculo, mexe em UM lugar só
#    (o método decorado), sem quebrar o código que já usa pessoa.idade

# --- POR QUE ISSO IMPORTA PRA VOCÊ ESPECIFICAMENTE ---
# No LabTrack, Pydantic (que você já usa nos schemas) usa muito esse
# princípio de encapsulamento por trás dos validators - e @property é comum
# em modelos SQLAlchemy quando você quer um campo "calculado" que não existe
# de verdade no banco de dados, tipo "dias_desde_cadastro" calculado a partir
# de uma data_cadastro armazenada.