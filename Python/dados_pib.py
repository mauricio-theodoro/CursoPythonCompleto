import pandas as pd  # Manipulação de dados
import numpy as np  # Operações numéricas
import matplotlib.pyplot as plt  # Gráficos
import seaborn as sns  # Gráficos estatísticos

# Configurar o estilo dos gráficos
sns.set_theme(style="whitegrid")

# Definir o caminho correto do arquivo
caminho_arquivo = r"C:\Users\Mauricio\Documents\CienciaDeDados\todos os arquivos\13.Prática em Python\dados\dados.csv"

# Carregar os dados corretamente (lembrando que pode estar separado por ponto e vírgula)
df = pd.read_csv(caminho_arquivo, delimiter=";")

# Exibir as primeiras 5 linhas
print(df.head())

# Ver informações gerais sobre os dados
print(df.info())

# Ver quantidade de valores nulos por coluna
print("\nValores Nulos:")
print(df.isnull().sum())

# Ver quantas duplicatas existem
print("\nValores Duplicados:")
print(df.duplicated().sum())


# Estatísticas descritivas das colunas numéricas
print(df.describe())

# Criar histogramas das colunas numéricas
df.hist(figsize=(10, 6), bins=20, color='skyblue', edgecolor='black')
plt.suptitle("Distribuição das Variáveis", fontsize=16)
plt.show()


# Criar boxplots para detectar outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.select_dtypes(include=['float64', 'int64']), palette="Set2")
plt.title("Boxplot das Variáveis Numéricas")
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["PIB"], y=df["VALOREMPENHO"], hue=df["MUNICIPIO"], palette="viridis", legend=False)
plt.xlabel("PIB")
plt.ylabel("Valor Empenhado")
plt.title("Relação entre PIB e Valor Empenhado por Município")
plt.grid(True)
plt.show()

df_sorted = df.sort_values(by="PIB", ascending=False)  # Ordena pelo PIB
plt.figure(figsize=(12, 6))

plt.barh(df_sorted["MUNICIPIO"], df_sorted["PIB"], color="royalblue", label="PIB")
plt.barh(df_sorted["MUNICIPIO"], df_sorted["VALOREMPENHO"], color="orange", label="Valor Empenhado", alpha=0.7)

plt.xlabel("Valores")
plt.ylabel("Municípios")
plt.title("Comparação PIB x Valor Empenhado", fontsize=14)
plt.legend()
plt.show()



