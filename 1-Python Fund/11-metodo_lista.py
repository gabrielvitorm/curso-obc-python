game_list = ["Fifa 23", "League of Legends", "The Last of Us 2", "God of War"]
print(game_list)

# 1 - Tamanho da lista
print(len(game_list))

# 2 - Recupera um item da lista pelo índice
print(game_list.index("League of Legends"))

# 3 - Adiciona item ao final da lista
game_list.append("Gta V")
print(game_list)

# 4 - Ordena lista
game_list.sort()
#listaJogos.reverse()
print(game_list)

# 5 - Copia os itens de uma lista para outra
game_reset = game_list.copy()
game_reset.remove('Fifa 23')
game_reset.remove('God of War')
print(game_reset)

# 6 - Remove todos os itens da lista
game_list.clear()
print(game_list)