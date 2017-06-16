# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:45:28 2017

@author: ALLALENA
"""

## Linear Regression using Gradient Descent
## Stochastic Gradient Descent is an important and widely used algorithm in machine learning.
## We will discover how to use Stochastic Gradient Descent to learn the coefficient
## for a simple linear regression model by minimizing the error on a training dataset
## Learn How stochastic gradient descent can be used to search for the coecients of a regression model.
## Learn How repeated iterations of gradient descent can create an accurate regression model.

import matplotlib.pyplot as plt
import math

def LRGradientDesc():
    xList = [1, 2, 4, 3, 5] #Input variables
    yList = [1, 3, 3, 2, 5] #Output variables
    # Gradient Descent is the process of minimizing a function by following the gradients of the cost function
    # w = w - alpha * delta where w is weight or coefficient been optimized.
    # alpha is a learning rate that we must configure (e.g. 0.1) and delta is the error for the model on the
    # the training data attributed to the weight w.
    # y = b0 + B1*x
    # Gradient descent iteration 1
    # B0 = 0
    # B1 = 0
    # Pi = yPredicted = 0 + 0 * 1 = 0
    # error = Ypredicted - yvalue = 0 - 1 = -1
    # We can now use this error in our equation for gradient descent to update the weights.
    # B0(t + 1) = Bo(t) - alpha * error
    
    B0 = 0.0
    B1 = 0.0
    alpha = 0.01
    error = 0
    b0List = []
    b1List = []
    errorList = []
    counter = 0
    
    
    while (counter < 4):
        for i, j in zip( xList, yList):
            ypred = B0 + B1 * j
            error = ypred - j
            errorList.append(error)
            B0 = B0 - alpha*error
            B1 = B1 - alpha*error*i
            b0List.append(B0)
            b1List.append(B1)
        counter = counter + 1
    print(b0List)
    print('----------------------------------------------------------------------------------------------------------------')
    print('----------------------------------------------------------------------------------------------------------------')
    print(b1List)
    
    plt.plot(errorList) #line plot
    plt.xlabel('')
    plt.ylabel('Error values')
    plt.show()
    
    lastB0Value = b0List[-1] 
    lastB1Value = b1List[-1] 
    print(lastB0Value, lastB1Value)
    
    #Once we minimized our B0 and B1 Lets clculate the predictions now
    predictions = []
    squareError = []
    for x, y in zip(xList, yList):
        predictions.append(lastB0Value + lastB1Value * x)   
        squareError.append( ((lastB0Value + lastB1Value * x) - y )**2   )
        
    print(predictions)
    print(squareError)
    
    # Now lets compute RMSE.
    RMSE = math.sqrt(sum(squareError)/len(squareError))
    print(RMSE)
    
    plt.plot(xList, predictions, 'bo')
    plt.plot(xList, yList, 'ro')
    plt.xlabel('x values')
    plt.ylabel('Y values - Predicted in red and y in blue')
    plt.show()
        
    #from looking at the plot we get a linear looking predicted values of Y   

LRGradientDesc()