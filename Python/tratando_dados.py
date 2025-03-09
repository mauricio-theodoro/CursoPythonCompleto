import pandas as pd

# 🔹 Caminho do arquivo CSV (use 'r' para evitar problemas com barras invertidas)
caminho_arquivo = r"C:\Users\Mauricio\Documents\CienciaDeDados\todos os arquivos\10.Prática em Python\dados\tempo.csv"

# 🔹 Carregar o CSV corretamente
df = pd.read_csv(caminho_arquivo, sep=";", encoding="utf-8")

# 🔹 Exibir estrutura inicial do DataFrame
print("\n📌 Antes do tratamento:")
print(df.info())

# 1️⃣ **Padronizar nomes das colunas**
df.columns = df.columns.str.lower().str.strip()

# 2️⃣ **Corrigir valores extremos sem excluir todas as linhas**
df["temperatura"] = df["temperatura"].astype(float)  # Converte para float antes da substituição
df.loc[df["temperatura"] > 50, "temperatura"] = df["temperatura"].median()  # Substituir valores absurdos por mediana
df.loc[df["umidade"] > 100, "umidade"] = 100  # Limitar umidade a 100%

# 3️⃣ **Corrigir possíveis erros de digitação na coluna 'aparencia'**
df["aparencia"] = df["aparencia"].replace({"menos": "nublado"})

# 4️⃣ **Preencher valores ausentes**
df["umidade"] = df["umidade"].fillna(df["umidade"].median())  # Substituir NaN pela mediana

# 🔹 Se houver moda na coluna "vento", usar esse valor; senão, definir "desconhecido"
moda_vento = df["vento"].mode()
df["vento"] = df["vento"].fillna(moda_vento[0] if not moda_vento.empty else "desconhecido")

# 5️⃣ **Padronizar colunas categóricas**
df["vento"] = df["vento"].str.lower().str.strip()
df["jogar"] = df["jogar"].str.lower().str.strip()
df["aparencia"] = df["aparencia"].str.lower().str.strip()

# 🔹 Exibir estrutura pós-tratamento
print("\n✅ Depois do tratamento:")
print(df.info())

# 🔹 Exibir os primeiros registros para conferência
print("\n🔎 Primeiras linhas do DataFrame tratado:")
print(df.head())
