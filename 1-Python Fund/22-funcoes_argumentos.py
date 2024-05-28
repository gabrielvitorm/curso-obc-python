#Crie uma função que recebe 2 argumentos: O primeiro nome e o Segundo nome
def full_name(fname, lname):
    print(f"Nome Completo: {fname} {lname}")
full_name("Gabriel", "Chaves")

#2 - Crie uma função que some 2 números via parâmetros
def sum(a, b):
    return a + b
print(sum(10, 50))

#3 - Argumentos default em uma função
def address(country="Brasil"):
    print(f"Eu moro no {country}")
address()
address("Canadá")

#4 - Avaliação do Jogo
def rating_game(qtd_rating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtd_rating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtd_rating}")
rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(rating)