import pprint

games_dict = {
    "Residente Evil 4":{
        "year_launch": 2023,
        "classification": 9.5,
        "genre": ["aventura", "ação"]
    },
    "God of War":{
        "year_launch": 2022,
        "classification": 9.8,
        "genre": ["aventura", "combate"]
    },
    "Fifa 23":{
        "year_launch": 2022,
        "classification": 8.3,
        "genre": ["esporte", "futebol"]
    },
    "League of Legends":{
        "year_launch": 2012,
        "classification": 7.9,
        "genre": ["MOBA", "estratégia"]
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(games_dict)

# 1 - Buscar informações dentro de um dicionário aninhado
print(games_dict["League of Legends"]["genre"])

# 2 - Adicionar novo item
games_dict["God of War"]["players"] = 1
print(games_dict["God of War"])

# 3 - Excluir dicionário
del games_dict["League of Legends"]
pp.pprint(games_dict)