# teste 1 random_state = 0	
## Acurácia	
KNN:	0.601398601
Árvore de Decisão:	0.622377622
Regressão Logistica:	0.678321678
## Precisão	
KNN:	0.557692308
Árvore de Decisão:	0.573770492
Regressão Logistica:	0.688888889
## Recall	
KNN:	0.46031746
Árvore de Decisão:	0.555555556
Regressão Logistica:	0.492063492

- Comecei modificando o Random State para verificar as alterações nos modelos.

# teste 2 eliminando alta cardinalidade	
## Acurácia	
KNN:	0.586592179
Árvore de Decisão:	0.670391061
Regressão Logistica:	0.731843575
## Precisão	
KNN:	0.5
Árvore de Decisão:	0.592592593
Regressão Logistica:	0.770833333
## Recall	
KNN:	0.351351351
Árvore de Decisão:	0.648648649
Regressão Logistica:	0.5

| Depois eliminei colunas com alta cardinalidade e substitui valores nulos de Age pela média.
| Também alterei o Random State para 42.
- Percebi que o modelo KNN teve uma perda de desempenho.
- Tive uma alta na quantidade de registros, isso provavelmente afetou o desempenho de ambos os modelos.

# Teste 3
## Acurácia dos modelos
KNN: 0.6223776223776224
Árvore de Decisão 0.6643356643356644
Regressão Logistica 0.6993006993006993

## Precisão dos Modelos
KNN:  0.5238095238095238
Árvore de Decisão:  0.5909090909090909
Regressão Logística:  0.6666666666666666

## Recall dos Modelos
KNN:  0.39285714285714285
Árvore de Decisão:  0.4642857142857143
Regressão Logística:  0.4642857142857143

- Percebi que ao posicionar mal a função para eliminar N/A, estava perdendo registros que fizeram diferença.

# Teste 4 891 registros

## Acurácia dos modelos
KNN: 0.664804469273743
Árvore de Decisão 0.6424581005586593
Regressão Logistica 0.7318435754189944


## Precisão dos Modelos
KNN:  0.6346153846153846
Árvore de Decisão:  0.5806451612903226
Regressão Logística:  0.7708333333333334


## Recall dos Modelos
KNN:  0.44594594594594594
Árvore de Decisão:  0.4864864864864865
Regressão Logística:  0.5

| Mantendo o mesmo padrão de 