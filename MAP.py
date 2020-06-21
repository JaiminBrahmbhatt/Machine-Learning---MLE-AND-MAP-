import pandas as pd

dataset_location ='D:\Masters\Machine Learning\Assignment\Assignment 1\HW1Data.csv'
dataset = pd.read_csv(dataset_location)
dirichlet_location = "D:\Masters\Machine Learning\Assignment\Assignment 1\DirichletData.csv"
dirichlet = pd.read_csv(dirichlet_location)

dirichlet_val = dirichlet['D4']
total_beta = sum(dirichlet_val)


frequencyx2 = ([363, 2119, 3375, 3571, 445, 1487])
total_alpha = sum(frequencyx2)

MAP_1 = ((frequencyx2[0] + dirichlet_val[0]) - 1)/ (total_alpha + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 0 and Y = -1 is ', MAP_1)

MAP_2 = ((frequencyx2[1] + dirichlet_val[1]) - 1) / (total_alpha + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 1 and Y = -1 is ', MAP_2)

MAP_3 = ((frequencyx2[2] + dirichlet_val[2]) - 1) / (total_alpha + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 2 and Y = -1 is ', MAP_3)

MAP_4 = ((frequencyx2[3] + dirichlet_val[3]) - 1) / (total_alpha + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 3 and Y = -1 is ', MAP_4)

MAP_5 = ((frequencyx2[4] + dirichlet_val[4]) - 1)/ (total_alpha + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 4 and Y = -1 is ', MAP_5)

MAP_6 = ((frequencyx2[5] + dirichlet_val[5]) - 1)/ (total_alpha + total_beta - 6)
print('The Maximum Posterior Probability of X2 = 5 and Y = -1 is ', MAP_6)


