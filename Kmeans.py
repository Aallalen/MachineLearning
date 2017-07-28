"""
FINAL PROJECT - PHASE 2
@author: ABDERREZAK ALLALEN
"""

import pandas as pd
import numpy as np
import os
import math

#Get working directory
os.getcwd() 
#Set 
u2=[]
u4=[]
col=[]
cluster_2=[]
cluster_4=[]
clust_2 = []
clust_4 = []
lstux=[[]]


#Load the csv file
def load_data(file):
    return pd.read_csv(file)
    
#Impute missing values
def impute_missing_value(raw_data):
    
    raw_data['A7'] = pd.to_numeric(raw_data['A7'], errors='coerce')
    raw_data["A7"].fillna(raw_data["A7"].mean(), inplace=True)  
    raw_data.A7 = raw_data.A7.astype(np.int64)
    
    return raw_data

#Calsculate euclidean distance        
def euclideanDistance(val1, val2):
	distance = 0
	for x in range(len(val1)):
		distance += pow((val1[x] - val2[x]), 2)
	return math.sqrt(distance) 

#Initialize first mean values and save it to a list
def initialize_mean(data, N):
    lst=[]
    ran = data.sample(n=N)
    u2 = list(ran.iloc[0])
    u4 = list(ran.iloc[1])
    lst.append(u2)
    lst.append(u4)
    return lst 

#Assign two clusters
def assignment(data, cluster_means):
    for index, row in data.iterrows():
        u2 = euclideanDistance(list(row)[1:10], cluster_means[0])
        u4 = euclideanDistance(list(row)[1:10], cluster_means[1])
   
        if u2 < u4:            
            data.set_value(index, 'PredClass', 2)
                  
        if u4 < u2:
            data.set_value(index, 'PredClass', 4)
                       
    return data
     
#Recalculate new means
def recalculationOfMeans(data):
    #Initiate lists for means 
    lstux1 =[]
    lstux2 =[]
    lstAll =[]
    df_2=data.loc[data['PredClass']==2]
    df_4=data.loc[data['PredClass']==4]    
    dfu2 = df_2.drop(['Scn','CLASS','PredClass'], axis=1)
    dfu4 = df_4.drop(['Scn','CLASS','PredClass'], axis=1)
    
    #Cluster 2 means
    for column in df_2.drop(['Scn','CLASS','PredClass'], axis=1).columns:
        lstux1.append(sum(dfu2[column])/dfu2[column].count())  
    lstAll.append(lstux1)
    
    #Cluster 4 means
    for column in df_4.drop(['Scn','CLASS','PredClass'], axis=1).columns:
        lstux2.append(sum(dfu4[column])/dfu4[column].count())           
    lstAll.append(lstux2)

    #Return recalculated clusters means
    return lstAll
    
    
def main():
    #Get raw data
    raw_data = load_data('BrestCancerData.csv')
    #Clean raw data and impute missing values
    data = impute_missing_value(raw_data)
    #Get clusters means
    clusters_means = initialize_mean(data.ix[:,1:10], 2)
    #Iterate 1500 times and recalculate clusters means and assign cluster to new data
    for i in range (1500):        
        data = assignment(data, clusters_means)
        clusters_means = recalculationOfMeans(data)
       
    #Print results            
    print('-------------------------Final mean------------------------')
    print('mu_2: ',clusters_means[0])
    print('mu_4: ',clusters_means[1])
    print('\n')
    print('--------------------Cluster assignment---------------------')
    print(data.iloc[:,[0,10,11]])
        
        
main()    
