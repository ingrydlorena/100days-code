import pandas as pd


table = pd.read_csv("cancelamentos.csv")
# axis = 1, reference to column

table = table.drop("CustomerID", axis =1)
print(table)
# remove rows with values null
table = table.dropna()
# shows information about the table
# print(table.info())
print(table['cancelou'].value_counts(normalize=True).map("{:.1%}".format))
print(table.groupby(['sexo','cancelou']).size())
