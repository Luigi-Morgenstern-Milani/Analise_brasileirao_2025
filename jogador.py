import pandas as pd
import os
import matplotlib.pyplot as plt


def ler_fbref_excel(path):
    df = pd.read_excel(path, header=[0,1], engine="openpyxl")

    df.columns = [
        col[1] if not str(col[1]).startswith("Unnamed") else col[0]
        for col in df.columns
    ]

   
    df.columns = df.columns.astype(str).str.replace("\u00a0"," ", regex=False).str.strip()

    
    df = df.dropna(axis=1, how="all")
    df = df.loc[:, ~df.columns.duplicated()]

    return df


def padronizar_coluna_player(df):
    for col in df.columns:
        if col.lower() == "player":
            df.rename(columns={col: "Player"}, inplace=True)
            return df
    
    df.rename(columns={df.columns[0]: "Player"}, inplace=True)
    return df

def converter_colunas_numericas(df):
    colunas_texto = ["Player","Nation","Pos","Squad","Comp","Age"]
    for col in df.columns:
        if col not in colunas_texto:
            try:
                df[col] = pd.to_numeric(df[col], errors="coerce")
            except Exception:
                pass
    return df


BASE_PATH = os.path.dirname(__file__)
standard_path = os.path.join(BASE_PATH, "Standard.xlsx")
shooting_path = os.path.join(BASE_PATH, "Shooting.xlsx")
passing_path  = os.path.join(BASE_PATH, "Passing.xlsx")
gca_path      = os.path.join(BASE_PATH, "Gca.xlsx")

standard = converter_colunas_numericas(padronizar_coluna_player(ler_fbref_excel(standard_path)))
shooting = converter_colunas_numericas(padronizar_coluna_player(ler_fbref_excel(shooting_path)))
passing  = converter_colunas_numericas(padronizar_coluna_player(ler_fbref_excel(passing_path)))
gca      = converter_colunas_numericas(padronizar_coluna_player(ler_fbref_excel(gca_path)))


df = (
    standard
    .merge(shooting, on="Player", how="left")
    .merge(passing,  on="Player", how="left")
    .merge(gca,      on="Player", how="left")
)


if "90s" in df.columns:
    df = df[df["90s"] >= 10]
else:
    df["90s"] = 1  


metricas = ["Gls","xG","Ast","SCA","GCA"]
metricas = [m for m in metricas if m in df.columns]

df_final = df.groupby("Player", as_index=False).agg({
    "90s": "sum",
    **{m: "sum" for m in metricas}
})

for m in metricas:
    df_final[f"{m}_90"] = df_final[m] / df_final["90s"]


pesos = {"xG_90":0.35, "Gls_90":0.25, "SCA_90":0.20, "Ast_90":0.15, "GCA_90":0.05}
score = 0

for col, peso in pesos.items():
    if col in df_final.columns:
        score += df_final[col] * peso

df_final["Score"] = score


top10 = df_final.sort_values("Score", ascending=False).head(10)

print("\nTOP 10 JOGADORES (IMPACTO POR 90 MIN):\n")
print(top10[["Player","Score"]])

plt.figure(figsize=(10,6))
plt.barh(top10["Player"], top10["Score"])
plt.xlabel("Score Ofensivo (por 90 min)")
plt.title("Top 10 Jogadores – Impacto por 90 min")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
