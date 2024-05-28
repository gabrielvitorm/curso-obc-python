game_fifa = {
    "name": "Fifa 23",
    "year_launch": 2022,
    "game_price": 90.50,
    "classification": 9.2,
    "genre": ["esporte", "família"]
}

print(game_fifa)
print(type(game_fifa))
print(len(game_fifa))

# 1 - Recuperando um elemento do dicionário
print(game_fifa['genre'])
print(game_fifa.get('classification'))

# 2 - Buscando apenas as chaves
print(game_fifa.keys())

# 3 - Buscando apenas os valores
print(game_fifa.values())

# 4 - Retorna itens do dicionário como tupla de uma lista 
print(game_fifa.items())

# 5 - Adicionando itens no dicionário
game_fifa["players"] = 2
print(game_fifa)

# 6 - Atualizando itens no dicionário
game_fifa.update({"players": 1})
print(game_fifa)

# 7 - Removendo item no dicionário
game_fifa.pop("players")
print(game_fifa)