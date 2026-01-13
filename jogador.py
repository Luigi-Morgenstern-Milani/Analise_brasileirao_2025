from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# FUNÇÃO PARA LIMPAR COLUNAS (PADRÃO FBREF)
# ==================================================
def ler_fbref_excel(path):
    """
    Lê arquivos do FBref com cabeçalho duplo
    e retorna DataFrame com colunas simples.
    """
    df = pd.read_excel(path, header=[0, 1])

    # Achata MultiIndex
    df.columns = [
        col[1] if col[1] != '' and not col[1].startswith('Unnamed')
        else col[0]
        for col in df.columns
    ]

    # Remove espaços invisíveis
    df.columns = df.columns.astype(str).str.strip()
    return df


# ==================================================
# CAMINHOS
# ==================================================
BASE_DIR = Path(__file__).resolve().parent

standard_path = BASE_DIR / "Standard.xlsx"
shooting_path = BASE_DIR / "Shooting.xlsx"
passing_path  = BASE_DIR / "Passing.xlsx"
gca_path      = BASE_DIR / "Gca.xlsx"

# ==================================================
# LEITURA DOS ARQUIVOS
# ==================================================
standard = ler_fbref_excel(standard_path)
shooting = ler_fbref_excel(shooting_path)
passing  = ler_fbref_excel(passing_path)
gca      = ler_fbref_excel(gca_path)

# ==================================================
# SELEÇÃO DE COLUNAS (CONFIRMADAS PELO SEU PRINT)
# ==================================================
standard = standard[['Player', 'Pos', '90s']].copy()
shooting = shooting[['Player', 'Sh', 'xG']].copy()
passing  = passing[['Player', 'KP']].copy()
gca      = gca[['Player', 'SCA']].copy()

# ==================================================
# MERGE DOS DADOS
# ==================================================
df = (
    standard
    .merge(shooting, on='Player')
    .merge(passing, on='Player')
    .merge(gca, on='Player')
)

df.dropna(inplace=True)

# ==================================================
# FILTRO DE MINUTAGEM
# ==================================================
df = df[df['90s'] >= 10]

# ==================================================
# MÉTRICAS POR 90
# ==================================================
df['xG_90']  = df['xG'] / df['90s']
df['Sh_90']  = df['Sh'] / df['90s']
df['KP_90']  = df['KP'] / df['90s']
df['SCA_90'] = df['SCA'] / df['90s']

# ==================================================
# NORMALIZAÇÃO (MIN-MAX)
# ==================================================
for col in ['xG_90', 'Sh_90', 'KP_90', 'SCA_90']:
    df[col + '_norm'] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# ==================================================
# ÍNDICE OFENSIVO (AUTORAL)
# ==================================================
df['Indice_Ofensivo'] = (
    0.4  * df['xG_90_norm'] +
    0.25 * df['Sh_90_norm'] +
    0.2  * df['SCA_90_norm'] +
    0.15 * df['KP_90_norm']
)

# ==================================================
# TOP 10
# ==================================================
top10 = df.sort_values('Indice_Ofensivo', ascending=False).head(10)

print("\nTOP 10 – ÍNDICE OFENSIVO\n")
print(top10[['Player', 'Pos', 'Indice_Ofensivo']])

# ==================================================
# GRÁFICO
# ==================================================
plt.figure(figsize=(10, 6))
plt.barh(top10['Player'], top10['Indice_Ofensivo'])
plt.title('Top 10 Jogadores – Índice Ofensivo')
plt.xlabel('Índice Ofensivo')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
