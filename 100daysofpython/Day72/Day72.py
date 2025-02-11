import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


music_data = pd.read_csv('music.csv')
music_data_update = music_data.drop(columns=['genre'])
drop_table = music_data['genre']


model = DecisionTreeClassifier()
model.fit(music_data_update, drop_table)


tree.export_graphviz(model, out_file="music-recommender.dot", feature_names=['age', 'gender'],
                     class_names= sorted(drop_table.unique()), label='all',
                     rounded=True, filled=True)


