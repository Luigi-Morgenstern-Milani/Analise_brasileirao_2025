
import os
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "stats.xlsx")

df = pd.read_excel(file_path)


df_raw = df.copy()



df = df[['Squad', 'MP', 'GF', 'GA', 'xG']]



df.rename(columns={
    'Squad': 'Time',
    'MP': 'Jogos',
    'GF': 'Gols_Feitos',
    'GA': 'Gols_Sofridos',
    'xG': 'xG'
}, inplace=True)



df['Jogos'] = df['Jogos'].astype(int)
df['Gols_Feitos'] = df['Gols_Feitos'].astype(int)
df['Gols_Sofridos'] = df['Gols_Sofridos'].astype(int)
df['xG'] = df['xG'].astype(float)

df.dropna(inplace=True)



df['Media_Gols_Feitos'] = df['Gols_Feitos'] / df['Jogos']
df['Media_xG'] = df['xG'] / df['Jogos']
df['Media_Gols_Sofridos'] = df['Gols_Sofridos'] / df['Jogos']

print("\nDESVIOS PADRÃO:")
print("Gols Feitos:", df['Gols_Feitos'].std())
print("xG:", df['xG'].std())
print("Gols Sofridos:", df['Gols_Sofridos'].std())



print("\nTABELA FINAL DO BRASILEIRÃO 2025:\n")
print(df.to_string(index=False))


df_gf = df.sort_values(by='Gols_Feitos', ascending=False)

plt.figure()
plt.barh(df_gf['Time'], df_gf['Gols_Feitos'])
plt.title('Ranking de Gols Feitos - Brasileirão 2025')
plt.xlabel('Gols Feitos')
plt.ylabel('Times')
plt.gca().invert_yaxis()
plt.show()



df_xg = df.sort_values(by='xG', ascending=False)

plt.figure()
plt.barh(df_xg['Time'], df_xg['xG'])
plt.title('Ranking de xG Acumulado - Brasileirão 2025')
plt.xlabel('xG')
plt.ylabel('Times')
plt.gca().invert_yaxis()
plt.show()


df_ga = df.sort_values(by='Gols_Sofridos')

plt.figure()
plt.barh(df_ga['Time'], df_ga['Gols_Sofridos'])
plt.title('Ranking de Gols Sofridos - Brasileirão 2025')
plt.xlabel('Gols Sofridos')
plt.ylabel('Times')
plt.gca().invert_yaxis()
plt.show()
