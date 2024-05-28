name = input("Digite o nome do jogo:\n")
year_launch = int(input("Digite o ano de lançamento do Jogo:\n"))
classification = float(input("Qual a classificação do jogo?\n"))

# Quando usamos o 'or' apenas um dos requisitos tem que ser cumpridos, quando usamos 'and' os dois requisitos tem que ser cumpridos
if classification > 8.0 or year_launch > 2018:
    print(f"O jogo {name} é bom! Recomendo jogá-lo")
else:
    print(f"O jogo {name} ainda não atingiu uma boa nota, por isso recomendo não jogá-lo")