Qual K teve melhor desempenho?
Geralmente, $K = 3$ ou $K = 5$ apresentam o melhor desempenho e maior poder de generalização. O $K=1$ tende a ficar muito exposto a ruídos nos dados de treino.

Qual métrica obteve melhor resultado?
A distância Euclidiana e a Manhattan costumam empatar ou apresentar resultados extremamente próximos (frequentemente acima de 95% de acurácia após a normalização),com uma leve vantagem para a Euclidiana dependendo da semente aleatória da divisão.

O que aconteceu com K muito pequeno?
Com $K = 1$ (K muito pequeno), o modelo sofre o risco de overfitting (sobreajuste). Ele se torna extremamente sensível a outliers e ruídos locais nos dados de treino, gerando fronteiras de decisão muito complexas e menos robustas para dados novos.

Por que normalizar é importante?
Porque o KNN se baseia no cálculo de distâncias geométricas entre os pontos. No dataset de câncer de mama, algumas características possuem valores na casa dos milhares (ex: área do tumor) e outras possuem valores menores que 1 (ex: suavidade). Se não normalizarmos com o StandardScaler, as variáveis de maior escala vão dominar completamente o cálculo da distância, fazendo com que as outras variáveis sejam ignoradas pelo algoritmo.
