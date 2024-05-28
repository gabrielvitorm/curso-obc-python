games_set = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}
print(games_set)
print(len(games_set))

# 1 - True e 1 são considerados o mesmo valor
example_set = {"Fifa23", True, 1, 90.50} 
print(example_set)

# 2 - Adicionando item no set
games_set.add("Resident Evil 4")
print(games_set)

# 3 - Adicionando item de outro set
games_set.update(example_set)
print(games_set)

# 4 - Remove um item no set
games_set.remove(True)
games_set.remove(90.5)
print(games_set)

# 5 - Não possibilita recuperar valores no set via slice