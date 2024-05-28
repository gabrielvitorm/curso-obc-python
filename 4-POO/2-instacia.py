class Movie:
    name = ""
    year_launch = 0
    include_plan = False
    note = 0
    duration_minutes = 0    

# Primeiro Filme
movie = Movie()
movie.name = "A Volta dos Que Não Foram"
movie.year_launch = 2024
movie.include_plan = True
movie.note = 5.0
movie.duration_minutes = 120

# Segundo Filme
movie2 = Movie()
movie2.name = "Resgate do Soldado Ryan"
movie2.year_launch = 2010
movie2.include_plan = False
movie2.note = 5.0
movie2.duration_minutes = 180

print("##Dados do Primeiro Filme##")
print(f"Nome do filme: {movie.name} \n Ano de Lançamento: {movie.year_launch} \n Está Incluso no Plano: {movie.include_plan} \n Nota do Filme: {movie.note} \n Duração do Filme: {movie.duration_minutes} Minutos.")

print("##Dados do Segundo Filme##")
print(f"Nome do filme: {movie2.name} \n Ano de Lançamento: {movie2.year_launch} \n Está Incluso no Plano: {movie2.include_plan} \n Nota do Filme: {movie2.note} \n Duração do Filme: {movie2.duration_minutes} Minutos.")