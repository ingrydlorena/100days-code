'''
Day 91: Data science
Use Python for data science projects (e.g., data cleaning, feature engineering).
'''
import pandas as pd
import numpy as np

data = {'Nome' :['Alice','Bob','Carlos','Daniela','Eduardo','Fernanda','Gabriel', 'Heloisa','Igor','Juliana'],
        'Idade' : [25.0,30.0,35.0, None, 45.0, 50.0, 28.0,33.0,40.0, 25.0],
        'Salario':[ 50000.0, 60000.0, 70000.0, 80000.0, 95000.0, 48000.0, None, 85000.0,76000.0, None], 
        'Departamento' : ['TI','RH','TI','Vendas', None, 'TI', 'Vendas', None,'RH','TI'],
        'Experiencia' : [2.0, 5.0, 7.0, None,15.0,3.0,8.0,6.0,None,12.0]}


df = pd.DataFrame(data)

# Cleaning None rows
df.dropna(inplace=True)
print("Data\n", df)

# Create a new table with the dataas
df["Salario_por_ano"] =df["Salario"] / df["Experiencia"]
df["Faixa_Idade"] = pd.cut(df["Idade"], bins=[20,30,40,50,60], labels=["Jovem","Adulto","Meia-idade", "Sênior"])
print(df)

label_enconder = LabelEnconder()


