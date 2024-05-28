teams = {}
done = False

# Função adicionar times
def add_teams():
    print("Função de adicionar times")
    qtd_teams = int(input("Digite a quantidade de times que você quer adicionar:\n"))
    for i in range(qtd_teams):
        team_name = input(f"Digite o nome do {i+1}° time: ")
        teams[team_name] = {'name': team_name, 'players': []}
        print("Time adicionado.")

# Função de Remover time
def rem_teams():
    print("Função de remover times")
    print_teams()
    team_num = int(input("Informe o número do time para remover: "))
    if team_num <= len(teams):
        team_name = list(teams.keys())[team_num-1]
        del teams[team_name]
        print("Time removido.")
    else:
        print("Número de time inválido.")

# Função de adicionar jogadores a um time
def add_player():
    print_teams()
    team_num = int(input("Informe o número do time que deseja adicionar jogador: "))
    if team_num <= len(teams):
        team_name = list(teams.keys())[team_num-1]
        qtd_players = int(input("Digite a quantidade de jogadores que você deseja adicionar: "))
        for i in range(qtd_players):
            player_name = input(f"Informe o nome do {i + 1}° jogador: ")
            teams[team_name]['players'].append(player_name)
            print("Jogador adicionado no time.")
    else:
        print("Número do time inválido")

# Função de remover Jogadores de um Time
def rem_players():
    print_teams()
    team_num = int(input("Informe o número do time que deseja remover jogador: "))
    if team_num <= len(teams):
        team_name = list(teams.keys())[team_num-1]
        print_team_players()
        player_num = int(input("Informe o número do jogador para remover: "))
        if player_num <= len(teams[team_name]['players']):
            del teams[team_name]['players'][player_num-1]
            print("Jogador removido do time.")
        else:
            print("Número do jogador inválido.")
    else:
        print("Número do time inválido.")


# Função de Listar
def print_teams():
    print("Times listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# função para listar jogadores de um time
def print_team_players():
    print_teams()
    team_num = int(input("Informe o número do time para listar jogadores: "))
    if team_num <= len(teams):
        team_name = list(teams.keys())[team_num-1]
        print(f"Jogadores do {team_name}:")
        for i, player in enumerate(teams[team_name]['players']):
            print(f"{i+1}. {player}")
    else:
        print("Número do time inválido.")


while not done:
    print("O que você deseja fazer?")
    print("1 - Adicionar um time")
    print("2 - Remover um time")
    print("3 - Listar os times")
    print("4 - Adicionar jogador em um time")
    print("5 - Remover jogador em um time")
    print("6 - Listar jogadores de um um time")
    print("7 - Sair do programa")

    choice = input(">")
    if choice == "1":
        add_teams()
    elif choice == "2":
        rem_teams()
    elif choice == "3":
        print_teams()
    elif choice == "4":
        add_player()
    elif choice == "5":
        rem_players()
    elif choice == "6":
        print_team_players()
    elif choice == "7":
        done = True
    else:
        print("Opção inválida")