class Movie:
    def __init__(self, name, year_launch, plan_include, note, duration_minutes):
        self.name = name
        self.year_launch = year_launch
        self.plan_include = plan_include
        self.note = note
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Filme: {self.name}"
    def technical_sheet(self):
        print("## Dados do Filme ##")
        print(f"Nome do Filme: {self.name}")
        print(f"Ano de Lançamento do Filme: {self.year_launch}")
        print(f"Está Incluso no Plano: {self.plan_include}")
        print(f"Nota do Filme: {self.note}")
        print(f"Duração do Filme: {self.duration_minutes}\n")

movie = Movie("Super Mario", 2023, False, 10.0, 120)
movie2 = Movie("Top Gun Maverick", 2022, False, 9.0, 140)
movie.technical_sheet()
movie2.technical_sheet()