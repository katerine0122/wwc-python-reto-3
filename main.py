import pandas as pd

def analizar_peliculas():
    df = pd.read_csv('movies_metadata.csv', sep=',')

    result = df[(df.revenue > 2000000) & (df.budget < 1000000)][[
        'title', 'release_date', 'budget', 'revenue', 'runtime']]

    return result


if __name__ == '__main__':
    peliculas_resultantes = analizar_peliculas()
    assert isinstance(peliculas_resultantes, pd.DataFrame), "Tu función aun no devuelve un Dataframe!"
    assert peliculas_resultantes.shape[1] == 5, "Verifica que tu Dataframe solo contenga las columnas mencionadas"
    assert peliculas_resultantes.shape[
               0] == 3, "Creo que debes verificar los filtros, la cantidad de películas que cumple las condiciones no es correcta"
    print("Excelente, has aprendido a leer CSV's con python y como filtrarlos!")
