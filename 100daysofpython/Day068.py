import matplotlib.pyplot as plt
import numpy as np
import pandas

xpoints = np.array([1, 5])
ypoints = np.array([1000, 5000])

table = pandas.read_csv("client.csv")
plt.rcParams['agg.path.chunksize'] = 100000

plt.plot(table['tempo_como_cliente'], table['total_gasto'], 'o')

plt.title('Vendas ao Longo dos Anos')
plt.xlabel('Client time')
plt.ylabel('Spend')

plt.show()







