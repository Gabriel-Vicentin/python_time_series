#V1.1

# EM python, o que é um cabeçalho do arquivo, para que ele serve? Qual a diferença entre um cabeçalho do arquivo para uma docstring? Para que serve uma docstring


#Docstring: Docstrings são maneiras de comentar durante o código, normalmente feitas nos módulos, packages, crates. é Possível também ser acessada durante o período de funcionamento do código, possibilitando a criação de funções extras para prestar ajuda em relação a documentação.
#Cabeçalho: É uma maneira de identificar o arquivo, seu criador, versão, descrição básica, contato, data de criação. É utilizado para dar um contexto geral do código.
#A grande diferença é a forma que utilizamos ambas, docstrings utilizamos para comentar durante o código, com o intuito de deixar a execução mais limpa e clara. Já o cabeçalho é um contexto geral antes de utilizarmos o arquivo.



# formate o cabeçalho deste arquivo, depois implemente as funções abaixo

def maximo(nums):
    """oque faz
    oque recebe
    oque retorna"""
    # TODO: percorra a lista guardando o maior atual
    ...
def e_par(n: int) -> bool:
    """ ... """
    # TODO: retorne se n é par
    ...
def fatorial(n: int) -> int:
    """   ...  """
    # TODO: implemente de forma iterativa (sem recursão)
    ...
