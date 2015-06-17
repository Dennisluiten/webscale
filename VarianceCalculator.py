# -*- coding: utf-8 -*-
"""
Created on Fri May 22 10:25:15 2015

@author: Dennis
"""
import random
import math

def updateSV(newData, S, mean, n):
    n += 1
    newmean = mean + (newData-mean)/n
    S += (newData-mean)*(newData-newmean)
    if(n > 1):
        variance = S/(n-1)
    else:
        variance = 0
    return (variance, S, newmean, n)
    
def streamingVariance():  
    mu = 10
    sigma = 5
    firstInput = random.gauss(mu, sigma)
    S = 0
    mean = firstInput
    n = 1
    variance = 0
    for x in range(1000000):   
        x = random.gauss(mu, sigma)
        (variance, S, mean, n) = updateSV(x, S, mean, n)
    print(variance)
    print (mean)
    print (S)
    print (n)
    
    
class feature:
    def __init__(self, mu, sigma, beta):
        self.n = 0
        self.mu = mu
        self.sigma = sigma
        self.beta = beta
        self.obsMu = 0
        self.obsVar = 0
        self.obsCov = 0
         
        
    def update(self, dataPoint, dy):
        self.n += 1
        dx = dataPoint - self.obsMu
        self.obsVar += (((self.n-1)/self.n)*dx*dx - self.obsVar)/self.n    
        self.obsCov += (((self.n-1)/self.n)*dx*dy - self.obsCov)/self.n
        self.obsMu += dx/self.n
        
    def getRandomInstance(self):
        return random.gauss(self.mu, self.sigma)
        
    def getBeta(self):
        return self.beta        
        
    def getB(self):
        return self.obsCov/self.obsVar
    
    
def linearRegression():
    print("Linear Regression")
    f1 = feature(10,1,0.5)
    f2 = feature(0,1, 0)
    intercept = 0
    noiseSigma = 0
    meanY = 0
    
    for n in range(1, 200000):
        nextF1 = f1.getRandomInstance()
        nextF2 = f2.getRandomInstance()
        newY = nextF1*f1.beta + nextF2*f2.beta + random.gauss(intercept, noiseSigma)
        dy = newY - meanY        
        f1.update(nextF1, dy)
        f2.update(nextF2, dy)        
        meanY += newY/n
        
    print("f1 B = {}".format(f1.getB()))
    print("f2 B = {}".format(f2.getB()))




#linearRegression()
    
    