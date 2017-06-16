# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:13:26 2017

@author: ALLALENA
"""

## Linear Regression
## a model that assumes linear relationship between input variable (x) 
## and the single output variable (y)
## y = b0 + b1*X Where y is predicted output, x is input value and b0 and b1 are coefficients
## when coefficient = 0 it willl remove the influence of the input variable on the model and therefor y = 0
## Example: y = b0 + b1* x   <=> weight = bo + b1*Height
## where bo is bias coefficient and b1 is the coefficient for the height column.
## We can use a learning technique to find a good set of coefficient values. 
## Once found, once found we can plug in deifferent height values to predict the weight.
## Let's say b0 = 0.1 and b1 = 0.5 so lets predict the weight in kg for a person
## with height of 182 => weight = 0.1 + 0.5 * 182 = 91.1

import matplotlib.pyplot as plt
import math


#xList = [1, 2, 4, 3, 5] #Input variables
#yList = [1, 3, 3, 2, 5] #Output variables

#plt.plot(xList, yList, 'ro')
#plt.xlabel('x Values')
#plt.ylabel('Y values')
#plt.show()

#Implementing linear regression from scratch

import numpy
#numpy.mean([1, 3, 3, 2, 5])
def mean(lst):
    return sum(lst)/len(lst)

## Now lets predict yList
def computeBOne():
    xList = [1, 2, 4, 3, 5] #Input variables
    yList = [1, 3, 3, 2, 5] #Output variables
    #y = Bo + B1*x
    #Calculate b1 and B0
    B1 = 0
    B0 = 0
    lst_nominator = []
    lst_denominator = []
    for i, j  in zip(xList, yList):
        lst_nominator.append((i - mean(xList) ) * (j - mean(yList)))
    print (lst_nominator)      
            
    for i in xList:
        lst_denominator.append((i - mean(xList))**2)
    
    print(lst_denominator)
    
    B1 = sum(lst_nominator) / sum(lst_denominator)
    print(B1) 

    B0 = mean(yList)  - B1 * mean(xList)
    
    #Making prediction using linear regression by using y = B0 + B1*x where
    #y is the predicted value
    print(B0)
    predictedY = []
    for x in xList:
        predictedY.append(B0 + B1*x)
        
    print(predictedY)
    plt.plot(xList, predictedY, 'ro')
    plt.xlabel('x Values')
    plt.ylabel('Predicted Y values')
    plt.show()    
       
    ## Estimating eror
    errorList = []
    RMSE = 0
    for yp, y in zip(predictedY, yList):
        errorList.append((yp - y)**2) #squared error
    # We can calculate an error score for our predictions called the Root Mean Squared Error or
    # RMSE.
    RMSE = math.sqrt(sum(errorList)/len(errorList)) # Meaning each prediction is on average wrong by RMSE value
    
    print(RMSE)
        
    #Shortcut for computing B1 is B1 = corr(x, y) * (stdev(y)/stdev(x))
    B1_2 = 0
    B1_2 = numpy.corrcoef(xList,yList)[0, 1]
    B1_3 = ((numpy.std(yList)/numpy.std(xList)))
    print(B1_2 * B1_3) # B1 = 0.8
        
computeBOne()



        

    


