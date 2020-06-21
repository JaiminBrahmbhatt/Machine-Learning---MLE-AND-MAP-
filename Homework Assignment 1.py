import pandas as pd

dataset_csv_url ='https://raw.githubusercontent.com/JaiminBrahmbhatt/Machine-Learning---MLE-AND-MAP-/master/HW1Data.csv'
dataset = pd.read_csv(dataset_csv_url)
dirichlet_location ="https://raw.githubusercontent.com/JaiminBrahmbhatt/Machine-Learning---MLE-AND-MAP-/master/DirichletData.csv"
#dirichlet_location = "D:\Masters\Machine Learning\Assignment\Assignment 1\DirichletData.csv"
dirichlet = pd.read_csv(dirichlet_location)

print('# Question 1')
print('The number of attributes of X1 with y = -1 and y = 1 respectively are :')
print(dataset.groupby('ClassLabel')['X1'].nunique())
print('The values of the attributes for X1 with y = -1 and y = 1 are :')
print(dataset['X1'].unique())
print('\n')
print('The number of attributes of X2 with y = -1 and y = 1 respectively are :')
print(dataset.groupby('ClassLabel')['X2'].nunique())
print('The values of the attributes for X2 with y = -1 and y = 1 are :')
print(dataset['X2'].unique())


count = dataset.groupby('X1')['ClassLabel'].value_counts()
count2 = dataset.groupby('X2')['ClassLabel'].value_counts()

print('\n')
print('# Question 2')
print('The frequency of values of X1 w.r.t y = -1 and y =1 respectively are:')
print(count)
print('The frequency of values of X2 w.r.t y = -1 and y =1 respectively are:')
print(count2)

print('\n')
print('# Question 3')
frequencyx1 = ([133, 447, 64, 485, 930, 893, 52, 120, 258, 57, 159, 2, 97, 3])
totalalpha = sum(frequencyx1)

MLE0 = frequencyx1[0] / totalalpha
print('MLE of X1=0 and y=1 is :', MLE0)

MLE1 = frequencyx1[1] / totalalpha
print('MLE of X1=1 and y=1 is :', MLE1)

MLE2 = frequencyx1[2] / totalalpha
print('MLE of X1=2 and y=1 is :', MLE2)

MLE3 = frequencyx1[3] / totalalpha
print('MLE of X1=3 and y=1 is :', MLE3)

MLE4 = frequencyx1[4] / totalalpha
print('MLE of X1=4 and y=1 is :', MLE4)

MLE5 = frequencyx1[5] / totalalpha
print('MLE of X1=5 and y=1 is :', MLE5)

MLE6 = frequencyx1[6] / totalalpha
print('MLE of X1=6 and y=1 is :', MLE6)

MLE7 = frequencyx1[7] / totalalpha
print('MLE of X1=7 and y=1 is :', MLE7)

MLE8 = frequencyx1[8] / totalalpha
print('MLE of X1=8 and y=1 is :', MLE8)

MLE9 = frequencyx1[9] / totalalpha
print('MLE of X1=9 and y=1 is :', MLE9)

MLE10 = frequencyx1[10] / totalalpha
print('MLE of X1=10 and y=1 is :', MLE10)

MLE11 = frequencyx1[11] / totalalpha
print('MLE of X1=11 and y=1 is :', MLE11)

MLE12 = frequencyx1[12] / totalalpha
print('MLE of X1=12 and y=1 is :', MLE12)

MLE13 = frequencyx1[13] / totalalpha
print('MLE of X1=13 and y=1 is :', MLE13)

print('\n')
print('# Question 4')
frequencyx2 = ([363, 2119, 3375, 3571, 445, 1487])
totalalpha2 = sum(frequencyx2)

MLE0 = frequencyx2[0] / totalalpha2
print('MLE of X2=0 and y=-1 is :', MLE0)

MLE1 = frequencyx2[1] / totalalpha2
print('MLE of X1=1 and y=-1 is :', MLE1)

MLE2 = frequencyx2[2] / totalalpha2
print('MLE of X2=2 and y=-1 is :', MLE2)

MLE3 = frequencyx2[3] / totalalpha2
print('MLE of X2=3 and y=-1 is :', MLE3)

MLE4 = frequencyx2[4] / totalalpha2
print('MLE of X2=4 and y=-1 is :', MLE4)

MLE5 = frequencyx2[5] / totalalpha2
print('MLE of X2=5 and y=-1 is :', MLE5)

print('\n')
print('#Question 5')
dirichlet_val = dirichlet['D6']
total_beta = sum(dirichlet_val)

MAP_1 = ((frequencyx2[0] + dirichlet_val[0]) - 1) / (totalalpha2 + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 0 and Y = -1 is ', MAP_1)

MAP_2 = ((frequencyx2[1] + dirichlet_val[1]) - 1) / (totalalpha2 + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 1 and Y = -1 is ', MAP_2)

MAP_3 = ((frequencyx2[2] + dirichlet_val[2]) - 1) / (totalalpha2 + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 2 and Y = -1 is ', MAP_3)

MAP_4 = ((frequencyx2[3] + dirichlet_val[3]) - 1) / (totalalpha2 + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 3 and Y = -1 is ', MAP_4)

MAP_5 = ((frequencyx2[4] + dirichlet_val[4]) - 1) / (totalalpha2 + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 4 and Y = -1 is ', MAP_5)

MAP_6 = ((frequencyx2[5] + dirichlet_val[5]) - 1) / (totalalpha2 + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 5 and Y = -1 is ', MAP_6)

