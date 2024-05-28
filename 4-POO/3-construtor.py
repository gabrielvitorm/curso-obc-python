class Movie:
    def __init__(self, name, year_launch, plan_include, note, duration_minutes):
        self.name = name
        self.year_launch = year_launch
        self.plan_include = plan_include
        self.note = note
        self.duration_minutes = duration_minutes

    def __str__(self):
        return f"Filme: {self.name}"

movie = Movie("Até o Último Homem", 2020, False, 5.0, 160)
print(movie)