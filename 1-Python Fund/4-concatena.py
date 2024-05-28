name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = bool(input("Está incluso no serviço mensal?\n"))

# Alternativa 1
# print("### Dados do Jogo###")
# print("====================")
# print("Nome do jogo:", name)
# print("Ano de Lançamento do jogo:", yearLaunch)
# print("Preço do jogo:", gamePrice)
# print("Está incluso no plano mensal:", planIncluded)

# Alternativa 2
# print("Nome do jogo:", name, "\n Ano de lançamento:", yearLaunch, "\n Preço do jogo: R$", gamePrice, "\n Está incluso no serviço?",  planIncluded)

# Alternativa 3
print(f"Nome do jogo: {name} \n Ano de lançamento: {yearLaunch} \n Preço do jogo: R$ {gamePrice} \n Está incluso no plano: {planIncluded}")