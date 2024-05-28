'''
Se estiver entre parenteses e tiver mais de um nome dentro do parenteses é considerado uma tupla, se tiver apenas um nome entre os parenteses é apenas uma string
'''
games_tuple = ("Fifa 23", "League of Legends", "The Last of Us 2", "God of War")
print(games_tuple)
print(type(games_tuple))

# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla

example_tuple = ("Fifa 23")
example_tuple2 = ("Fifa 23", 20, True )
print(type(example_tuple2))
print(example_tuple2)

# Busque os dois primeiros itens da lista
print(games_tuple[0:2])

# Busque o último item da lista
print(games_tuple[-1])

# Busca jogos até uma posição
print(games_tuple[:2])

# Busca jogos de uma posição em diante
print(games_tuple[2:])

# Recupera um item da tupla pelo índice
print(games_tuple.index("Fifa 23"))