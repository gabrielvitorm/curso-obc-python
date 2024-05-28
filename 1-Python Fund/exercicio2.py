""" 
Exercício 2:
*Substituindo caractere repetido:
-> Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
Ex:
fifa 23 → **fi#a 23**
restart→ resta#t
"""
gameName = input("Digite o nome do Jogo:\n")
gameDescription = """
O Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports,
e que possibilita jogar localmente ou online.
"""

"""
# Alternativa 1
print(gameName.replace("f", "$"))
print(gameDescription.replace("a", "$"))
"""
# Alternativa 2
char = gameName[0].lower()
new_name = gameName.replace(char, '$')
new_name = char + new_name[1:]
print(new_name)

char2 = gameDescription[0].lower()
new_description = gameDescription.replace(char2, '@')
new_description = char2 + new_description[1:]
print(new_description)

"""
*Substituindo caractere repetido
-> Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex:
abc xyz → **xyc abz**
"""
st1 = "cab"
st2 = "zyx"

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print(new_st1)
print(new_st2)