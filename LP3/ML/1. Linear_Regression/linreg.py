import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

data = pd.read_csv('data_back_pain.csv')
print(data.head())

data.plot(x='X',y='Y',style='o')
plt.title('Hours vs Backache Risk')
plt.xlabel('No. of hours driving')
plt.ylabel('Risk of backache')
plt.show()

