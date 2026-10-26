# Importando bibliotecas
import pandas as pd
import openpyxl

from sklearn.datasets import fetch_california_housing 

from joblib import load


# importando arquivos de teste.
housing = fetch_california_housing(as_frame=True)
print(housing.data.shape, housing.target.shape)
print(housing.feature_names[:])
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df['MedHouseVal'] = housing.target
df.head()


# Carregando modelo
reg = load(r'C:\Users\eledi\OneDrive - Cruzeiro do Sul Educacional - Acadêmico\Desktop\Cursa DataScience\Hashtag Programação\curso_data_science\modelos\regressao.joblib')

# Fazendo previsão 
X_teste = df.drop('MedHouseVal', axis=1)

# Exportando 
previsao = reg.predict(X_teste)

X_teste['Previsao'] = previsao
X_teste.to_excel(r'C:\Users\eledi\OneDrive - Cruzeiro do Sul Educacional - Acadêmico\Desktop\Cursa DataScience\Hashtag Programação\curso_data_science\Usuario\modelo_regressao.xlsx')