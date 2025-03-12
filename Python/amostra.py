import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Caminho do arquivo CSV
caminho_arquivo = r"C:\Users\Mauricio\Documents\CienciaDeDados\todos os arquivos\16.Prática em Python\dados\iris.csv"

# Ler os dados
df = pd.read_csv(caminho_arquivo)

# Mostrar as primeiras 5 linhas
print(df.head())

# Informações gerais sobre os dados
print(df.info())

# Estatísticas descritivas
print(df.describe())

# Verificar duplicatas
print(f"Linhas duplicadas: {df.duplicated().sum()}")

# Remover duplicatas (se houver)
df.drop_duplicates(inplace=True)

print(f"Linhas duplicadas: {df.duplicated().sum()}")

sns.boxplot(data=df)
plt.title("Verificação de Outliers")
plt.xticks(rotation=45)
plt.show()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df_normalizado = pd.DataFrame(scaler.fit_transform(df.iloc[:, :-1]), columns=df.columns[:-1])

sns.pairplot(df, hue="class")

plt.show()
