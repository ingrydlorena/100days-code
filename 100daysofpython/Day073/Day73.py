import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from sklearn.metrics import accurary_score

df = pd.read_csv('Churn.csv')

x = pd.get_dummies(df.drop(['Churn', 'Customer ID'], axis=1))
y = df['Churn'].apply(lambda x:1 if x=='Yes' else 0)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.2)
x_train.head()
y_train.head()



# Build and compile model
model = Sequential()
model.add(Dense(units=32, activation='relu', input_dim=len(x_train.columns)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='sgd', metrics='accuracy')

#fit, predict and evaluate
model.fit(x_train, y_train, epochs=200, batch_size=32)
y_hat = model.predict(x_test)
y_hat = [0 if val <0.5 else 1 for val in y_hat]


accurary_score(y_test, y_hat)
model.save('tfmodel')

# del model
# model = load_model('tfmodel')