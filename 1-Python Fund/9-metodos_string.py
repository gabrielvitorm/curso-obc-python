gameName = "Fifa 23"
gameDescription = """
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online.
"""

print(gameName.upper()) # Retornar string em maiúsculo
print(gameName.lower()) # Retornar string em minúsculo
print(gameName.capitalize()) # Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maiúsculo
print(gameName.center(11, '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("i")) # Retorna a posição de um determinado caractere 
print(gameName.count("f")) # Conta caracteres
print(gameDescription.count("f")) # Conta caracteres
print(gameDescription.count("a")) # Conta caracteres
print(gameDescription.replace("Fifa", "pes")) # Altera um elemento por outro
print(gameDescription.split(',')) # Quebra o texto na vírgula