'''
Day 75: Recommendation system
Build a recommendation system.
'''
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from scipy.sparse import csr_matrix

# Carregar os dados do MovieLens (substitua pelo caminho real do arquivo)
data = pd.read_csv('ratings.csv')

# Dividir os dados em conjuntos de treino e teste
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Criar a matriz de usuário-item (usuário como linhas, filmes como colunas)
train_user_item_matrix = train_data.pivot(index="userId", columns="movieId", values="rating").fillna(0)
test_user_item_matrix = test_data.pivot(index="userId", columns="movieId", values="rating").fillna(0)

# Converter a matriz de treino para formato esparso (CSR) para economizar memória
train_user_item_matrix_sparse = csr_matrix(train_user_item_matrix.values)

# Criar o modelo k-NN com similaridade cosseno
knn = NearestNeighbors(n_neighbors=5, metric="cosine", algorithm="auto")

# Ajustar o modelo k-NN com a matriz esparsa
knn.fit(train_user_item_matrix_sparse)

# Encontrar os 5 vizinhos mais próximos para cada usuário
distances, indices = knn.kneighbors(train_user_item_matrix_sparse)

# Obter os vizinhos mais próximos para o usuário 1
user_index = train_user_item_matrix.index.get_loc(1)  # Encontrar o índice do usuário 1
nearest_users = indices[user_index]

# Obter as classificações dos vizinhos mais próximos (para os filmes que eles classificaram)
nearest_users_ratings = train_user_item_matrix.iloc[nearest_users].mean(axis=0)

# Classificar as recomendações de filmes com base na maior média de classificações dos vizinhos
recommended_movies = nearest_users_ratings.sort_values(ascending=False).head(10)

print("Top 10 filmes recomendados para o usuário 1: ", recommended_movies)

# Agora, vamos avaliar o modelo no conjunto de testes
predicted_ratings = []

# Iterar sobre as linhas do conjunto de teste
for _, row in test_data.iterrows():
    user_id = row["userId"]
    movie_id = row["movieId"]

    # Verificar se o usuário está no conjunto de treino
    if user_id in train_user_item_matrix.index:
        user_index = train_user_item_matrix.index.get_loc(user_id)
        nearest_users = indices[user_index]

        # Verificar se o filme está no conjunto de treino
        if movie_id in train_user_item_matrix.columns:
            nearest_users_ratings = train_user_item_matrix.iloc[nearest_users, train_user_item_matrix.columns.get_loc(movie_id)]
            predicted_rating = nearest_users_ratings.mean()
            predicted_ratings.append(predicted_rating)

# Comparar as classificações previstas com as reais no conjunto de teste
actual_ratings = test_data["rating"].values

# Calcular RMSE (Root Mean Squared Error)
rmse = sqrt(mean_squared_error(actual_ratings, predicted_ratings))
print(f"RMSE: {rmse}")





