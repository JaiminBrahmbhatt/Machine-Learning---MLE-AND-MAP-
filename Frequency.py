import pandas as pd

dataset_csv_url ='https://raw.githubusercontent.com/JaiminBrahmbhatt/Machine-Learning---MLE-AND-MAP-/master/HW1Data.csv'
#gapminder_csv_url ='D:\Masters\Machine Learning\Assignment\Assignment 1\HW1Data.csv'
# load the data with pd.read_csv
dataset = pd.read_csv(dataset_csv_url)

count = dataset.groupby('X1')['ClassLabel'].value_counts()
count2 = dataset.groupby('X2')['ClassLabel'].value_counts()

print('The frequency of values of X1 w.r.t y = -1 and y =1 respectively are:')
print(count)
print('\n')
print('The frequency of values of X2 w.r.t y = -1 and y =1 respectively are:')
print(count2)