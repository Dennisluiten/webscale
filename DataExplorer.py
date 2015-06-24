# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:38:02 2015

@author: Dennis
"""
#import json
import serverHandler
import VarianceCalculator

#print (serverHandler.getData(1,1))
#print(serverHandler.submitResponse(1, 1, 5, "skyscraper", "green", 10, 10))

nrrunids = 5
nris = 5

sum = 0
mean = 0
n = 0
variance = 10

for runid in range (1, nrrunids):
    for i in range (1, nris):
        print ("Running for: {}".format(i))
        json = getData(runid,i) 
        nextData = json['context']['Age']
        (variance, S, mean, n) = VarianceCalculator.updateSV(nextData, sum, mean, n)
        
print(mean)
print(variance)