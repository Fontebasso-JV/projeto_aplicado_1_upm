# %%
# Importando pandas
import pandas as pd
import glob
import os

# %%
# Caminho arquivos Parquet
diretorio = r"data\sisvan.parquet"

# Usando glob para listar todos os arquivos .parquet no diretório
arquivos_parquet = glob.glob(os.path.join(diretorio, '*.parquet'))

# Criando df
df = pd.concat([pd.read_parquet(arquivo) for arquivo in arquivos_parquet])

# %%
df.head()
