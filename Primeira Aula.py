import pandas as pd

uri = 'https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula4.2/movies.csv'
filmes = pd.read_csv(uri)
filmes.head()

filmes.columns = ["filmesId", "titulo", "generos"]
filmes.head()

