
import pandas as pd

# 1 - Importar arquivo
arquivo_bruto = pd.read_csv(r"C:\\Users\\hugop\\OneDrive\\Desktop\\Dashboard - Recebimento\\recebimento.csv")
print(arquivo_bruto)

# 2 - Ler arquivo, removendo separadores para melhoria da apresentação (ex: ;./,-...)
print("Imprimindo dados com separadores: ';': ")
arquivo_bruto = pd.read_csv(r"C:\\Users\\hugop\\OneDrive\\Desktop\\Dashboard - Recebimento\\recebimento.csv",sep=";")
print(arquivo_bruto)

# 3 - Tratar dados, removendo dados nulos, espaços e células em branco

df = pd.read_csv(r"C:\\Users\\hugop\\OneDrive\\Desktop\\Dashboard - Recebimento\\recebimento.csv",sep=";")
print(df)

arquivo_tratado = df.dropna()
# remove valores nulos

arquivo_tratado = arquivo_tratado.map(lambda x: x.strip() if isinstance(x, str) else x )
print(arquivo_tratado)
# remove espaços

# 4 - Salvar novo arquivo tratado 
arquivo_tratado.to_csv(r"C:\\Users\\hugop\\OneDrive\\Desktop\\Dashboard - Recebimento\\recebimento_tratado.csv",sep=";",index=False)
print("✅ Arquivo tratado e gerado com sucesso")