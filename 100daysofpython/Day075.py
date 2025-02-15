'''
Day 75: Recommendation system
Build a recommendation system.
'''

# First open the data frame
import pandas as pd
movies_df = pd.read_csv("movies.csv")
rating_df = pd.read_csv("ratings.csv")

movies_names = movies_df.set_index("movieId")["title"].to_dict()
n_users = len(rating_df.userId.unique())
n_itens = len(rating_df.movieId.unique())
print("Number of unique users:", n_users)
print('-'*6)
print("Number of unique movies:", n_itens)
print('-'*6)
print("The full rating matrix will have:", n_users*n_itens,'elements')
print('-'*6)
print("Number of ratings:", len(rating_df))
print('-'*6)
print("Therefore:", len(rating_df)/ (n_users*n_itens) * 100, "% of the matrix is filled")

import torch
import numpy as np
from torch.autograd import Variable
from tqdm import tqdm


class MatrixFactorization(torch.nn.Module):
    def __init__(self, n_users, n_items, n_factors = 20):
        super().__init__()

        # create user embeddings
        self.user_factors = torch.nn.Embedding(n_users, n_factors) # think of this as lookup table for the input.
        # create item embbeddings
        self.item_factors = torch.nn.Embedding(n_items, n_factors) # think of this as lookup table for the input

        self.user_factors.weight.data.uniform_(0,0.05)
        self.item_factors.weight.data.uniform_(0,0.05)
    
    def forward(self, data):
        # matrix multiplication
        users, items = data[:,0], data[:,1]
        user_embeddings = self.user_factors(users)
        item_embeddings = self.item_factors(items)

        prediction =  ((user_embeddings * item_embeddings).sum(1))
        return prediction
    # def forwad(self, user, item)
    # matris multiplication
    # return (self.user_factors(user)*self.item_factors(item)).sum(1)

    def predict(self, user, item):
        return self.forwad(user, item)
    
from torch.utils.data.dataset import Dataset # necessary for PyTorch
from torch.utils.data import DataLoader # package that helps transform your data to machine learning readiness

class Loader(Dataset):
    def __init__(self):
        self.ratings = rating_df.copy()

        # Extract all user IDs and movie IDs
        users = rating_df.userId.unique()
        movies = rating_df.movieId.unique()

        # Unique values : index
        self.userid2idx = {o:i for i, o in enumerate(users)}
        self.movieid2idx = {o:i for i, o in enumerate(movies)}

        # Obtained continuous ID for users and movies
        self.idx2userid = {i:o for o,i in self.userid2idx.items()}
        self.idx2movieid = {i:o for o,i in self.movieid2idx.items()}


        # return the id from the indexed values as noted in the lambda function down below
        self.ratings.movieId = rating_df.movieId.apply(lambda x: self.movieid2idx[x])
        self.ratings.userId = rating_df.userId.apply(lambda x: self.userid2idx[x])


        self.x = self.ratings.drop(['rating', 'timestamp'], axis = 1).values
        self.y = self.ratings['rating'].values
        self.x, self.y = torch.tensor(self.x), torch.tensor(self.y)  # Transdorms the data to tensors (ready for torch models)

    def __getitem__(self, index):
        return (self.x[index], self.y[index])
    
    def __len__(self):
        return len(self.ratings)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print("Is running on GPU:", torch.cuda.is_available())

num_epochs = 128
model = MatrixFactorization(n_users, n_itens, n_factors=8)
model = model.to(device)  # Move o modelo para a GPU ou CPU
print(model)

# MSE loss
loss_fn = torch.nn.MSELoss()

# ADAM optimizer
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)


train_set = Loader()
train_loader = DataLoader(train_set, 128, shuffle=True)

for it in tqdm(range(num_epochs)):
    losses = []
    for x, y in train_loader:
        
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()  

        outputs = model(x)  
        loss = loss_fn(outputs.squeeze(), y.type(torch.float32)) 
        losses.append(loss.item())  

        loss.backward()  
        optimizer.step()  
        
    
    print("iter #{}".format(it), "Loss:", sum(losses) / len(losses))


c = 0
uw = 0
iw = 0
for name, param in model.named_parameters():
    if param.requires_grad:
        print(name, param.data)
        if c == 0:
            uw = param.data
            c +=1
        else:
            iw = param.data
        # print('param_data', param_Data)


# não terminei por motivos que estavam gerando erro e não estava entendendo mais nada depois eu volto nesse código quando tiver mais tempo