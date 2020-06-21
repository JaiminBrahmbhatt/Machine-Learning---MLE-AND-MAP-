import pandas as pd

dataset_csv_url ='https://raw.githubusercontent.com/JaiminBrahmbhatt/Machine-Learning---MLE-AND-MAP-/master/HW1Data.csv'
#gapminder_csv_url ='D:\Masters\Machine Learning\Assignment\Assignment 1\HW1Data.csv'
dataset = pd.read_csv(dataset_csv_url)

print('The number of attributes of X1 with y = -1 and y = 1 respectively are :')
print(dataset.groupby('ClassLabel')['X1'].nunique())
print('\n')
print('The values of the attributes for X1 with y = -1 and y = 1 are :')
print(dataset['X1'].unique())


print('\n')
print('The number of attributes of X2 with y = -1 and y = 1 respectively are :')
print(dataset.groupby('ClassLabel')['X2'].nunique())
print('\n')
print('The values of the attributes for X2 with y = -1 and y = 1 are :')
print(dataset['X2'].unique())



#method2

#data = dataset.groupby('ClassLabel')
#data = data.agg({"X2": "nunique"})
#print(data)

# Method 3
# print('The number of attributes of X1 and y=-1 are 14 :')
# print(dataset['X1'].unique())
# print('The number of attributes of X1 and y=1 are 14 :')
# print(dataset['X1'].unique())
# print('The number of attributes of X2 and y=-1 are 6 :')
# print(dataset['X2'].unique())
# print('The number of attributes of X2 and y=1 are 6 :')
# print(dataset['X2'].unique())