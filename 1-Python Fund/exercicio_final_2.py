import tkinter as Tk

class Time:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def remover_jogador(self, jogador):
        if jogador in self.jogadores:
            self.jogadores.remove(jogador)
        else:
            print(f"Jogador {jogador} não encontrado no time {self.nome}.")

    def listar_jogadores(self):
        if self.jogadores:
            print(f"Jogadores do time {self.nome}:")
            for jogador in self.jogadores:
                print(jogador)
        else:
            print(f"O time {self.nome} não possui jogadores.")

class GerenciadorTimes:
    def __init__(self):
        self.times = []

    def adicionar_time(self, nome):
        self.times.append(Time(nome))

    def remover_time(self, indice):
        if 0 <= indice < len(self.times):
            del self.times[indice]
        else:
            print("Índice inválido.")

    def listar_times(self):
        print("Times cadastrados:")
        for indice, time in enumerate(self.times):
            print(f"{indice}: {time.nome} - Jogadores: {len(time.jogadores)}")

    def adicionar_jogador_time(self, indice_time, jogador):
        if 0 <= indice_time < len(self.times):
            self.times[indice_time].adicionar_jogador(jogador)
        else:
            print("Índice de time inválido.")

    def remover_jogador_time(self, indice_time, jogador):
        if 0 <= indice_time < len(self.times):
            self.times[indice_time].remover_jogador(jogador)
        else:
            print("Índice de time inválido.")

    def listar_jogadores_time(self, indice_time):
        if 0 <= indice_time < len(self.times):
            self.times[indice_time].listar_jogadores()
        else:
            print("Índice de time inválido.")

# Funções para interação com a interface gráfica

def adicionar_time():
    nome_time = nome_time_entry.get()
    gerenciador.adicionar_time(nome_time)
    listar_times()

def remover_time():
    indice_time = int(indice_time_entry.get())
    gerenciador.remover_time(indice_time)
    listar_times()

def listar_times():
    times_text.delete(1.0, Tk.END)
    times_text.insert(Tk.END, "Times cadastrados:\n")
    for indice, time in enumerate(gerenciador.times):
        times_text.insert(Tk.END, f"{indice}: {time.nome} - Jogadores: {len(time.jogadores)}\n")

def adicionar_jogador_time():
    indice_time = int(indice_time_jogador_entry.get())
    jogador = nome_jogador_entry.get()
    gerenciador.adicionar_jogador_time(indice_time, jogador)

def remover_jogador_time():
    indice_time = int(indice_time_jogador_entry.get())
    jogador = nome_jogador_remover_entry.get()
    gerenciador.remover_jogador_time(indice_time, jogador)

def listar_jogadores_time():
    indice_time = int(indice_time_jogador_entry.get())
    jogadores_text.delete(1.0, Tk.END)
    jogadores_text.insert(Tk.END, f"Jogadores do time {gerenciador.times[indice_time].nome}:\n")
    for jogador in gerenciador.times[indice_time].jogadores:
        jogadores_text.insert(Tk.END, f"{jogador}\n")

# Configuração da interface gráfica

app = Tk.Tk()
app.title("Gerenciador de Times")

nome_time_label = Tk.Label(app, text="Nome do time:")
nome_time_label.pack()
nome_time_entry = Tk.Entry(app)
nome_time_entry.pack()

adicionar_time_button = Tk.Button(app, text="Adicionar Time", command=adicionar_time)
adicionar_time_button.pack()

indice_time_label = Tk.Label(app, text="Índice do time a ser removido:")
indice_time_label.pack()
indice_time_entry = Tk.Entry(app)
indice_time_entry.pack()

remover_time_button = Tk.Button(app, text="Remover Time", command=remover_time)
remover_time_button.pack()

listar_times_button = Tk.Button(app, text="Listar Times", command=listar_times)
listar_times_button.pack()

indice_time_jogador_label = Tk.Label(app, text="Índice do time:")
indice_time_jogador_label.pack()
indice_time_jogador_entry = Tk.Entry(app)
indice_time_jogador_entry.pack()

nome_jogador_label = Tk.Label(app, text="Nome do jogador:")
nome_jogador_label.pack()
nome_jogador_entry = Tk.Entry(app)
nome_jogador_entry.pack()

adicionar_jogador_button = Tk.Button(app, text="Adicionar Jogador ao Time", command=adicionar_jogador_time)
adicionar_jogador_button.pack()

nome_jogador_remover_label = Tk.Label(app, text="Nome do jogador a ser removido:")
nome_jogador_remover_label.pack()
nome_jogador_remover_entry = Tk.Entry(app)
nome_jogador_remover_entry.pack()

remover_jogador_button = Tk.Button(app, text="Remover Jogador do Time", command=remover_jogador_time)
remover_jogador_button.pack()

listar_jogadores_button = Tk.Button(app, text="Listar Jogadores do Time", command=listar_jogadores_time)
listar_jogadores_button.pack()

times_text = Tk.Text(app)
times_text.pack()

jogadores_text = Tk.Text(app)
jogadores_text.pack()

app.mainloop()
