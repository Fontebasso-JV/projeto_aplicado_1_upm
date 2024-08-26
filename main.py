# %%
# Importando pandas
import pandas as pd
import glob

# %%
# Criando df

csv_files = glob.glob('data/planos_saude_abrangencia_nacional/*.csv')
df = pd.concat([pd.read_csv(file, sep=';') for file in csv_files], ignore_index=True)

# %%
# Amostra dos dados
df.head(5)

# %%
# Metadados

df.dtypes

# %%
#