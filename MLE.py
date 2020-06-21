import pandas as pd

gapminder_csv_url ='https://raw.githubusercontent.com/JaiminBrahmbhatt/Machine-Learning---MLE-AND-MAP-/master/HW1Data.csv'
#gapminder_csv_url ='D:\Masters\Machine Learning\Assignment\Assignment 1\HW1Data.csv'
# load the data with pd.read_csv
record = pd.read_csv(gapminder_csv_url)


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

#frequencyx1 = record.groupby('ClassLabel')['X1'].value_counts(normalize =True)


#print(frequencyx1)

