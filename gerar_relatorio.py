
import pandas as pd
from time import sleep

arquivo_bruto = r"C:\\Users\\hugop\\OneDrive\\Desktop\\Dashboard - Recebimento\\export.csv"
print(arquivo_bruto)

sleep(2)
print("Lendo arquivo 'export.csv'...")
df = pd.read_csv(arquivo_bruto, sep=";", encoding = "latin1", header=None)
#encoding="latin1" informa ao Pandas qual codificação usar para interpretar corretamente os caracteres do arquivo,
# evitando erros de leitura como o UnicodeDecodeError.

print(df)

print("Remover cabeçalho: ")

sleep(2)
print("# 1. Selecionar somente a partir da linha 17")
df= df.iloc[17:]
print(df)

sleep(2)
print("# 2. Transformar a primeira linha restante em cabeçalho")
df.columns = df.iloc[0]
print(df)

sleep(2)
print("# 3. Remover a primeira linha, que agora está duplicada")
df = df.iloc[1:]
print(df)

print("📊 DIAGNÓSTICO DOS DADOS")

print("\nQuantidade de linhas e colunas:")
print(df.shape)

print("Quantidade de valores nulos por coluna:")
print(df.isna().sum())

print("Quantidade de linhas duplicadas:")
print(df.duplicated().sum())


sleep(2)
print("# 4. Gerando e salvando arquivo tratado")

df.to_csv(r"C:\\Users\\hugop\\OneDrive\\Desktop\\Dashboard - Recebimento\\recebimento_tratado.csv",
sep=";",
index =False,
encoding="utf-8-sig")

sleep(2)
print("✅'recebimento_tratado.csv', gerado com sucesso! ")
input("\n\n\n\n\nPressione ENTER para sair do programa.")