import pandas as pd

psg_players = pd.Series(
    ['Navas', 'Mbappe', 'Neymar', 'Messy'], 
    index=[1,7,10,30]
)

print(psg_players)

psg_players2 = pd.Series(['Navas', 'Mbappe', 'Neymar', 'Messy'])
print(psg_players2)

equipo = {
    'Jugador': ['Navas', 'Mbappe', 'Neymar', 'Messy'],
    'Altura': [183.0, 170.0, 165.0, 179.4],
    'Goles': [1, 200, 200, 100]
}

df_equipo = pd.DataFrame(equipo) # index=[1,7,10,30] se puede agregar indice


print(df_equipo)
print(df_equipo.columns)

