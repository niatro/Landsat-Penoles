import pandas as pd

# Leer el archivo de Excel
df = pd.read_excel("datos_landsat.xlsx")

# Convertir el dataframe a LaTeX
latex_table = df.to_latex(index=False)  # index=False para no incluir el índice del dataframe en la tabla

print(latex_table)
