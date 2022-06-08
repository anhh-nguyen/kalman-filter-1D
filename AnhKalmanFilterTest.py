# This is a Kalman Filter test for linear system. Find the exact location of the a vehicle

#import needed math function
from math import *
from statistics import variance
import matplotlib.pyplot as plt
import numpy as np


# In Kalman Filter, the distribution is Gaussian 
# gaussian def calculate the gaussian value of x using mean and variance
def gaussian(mean, variance, x):
    coefficient = 1.0 / sqrt(2.0 * pi * variance)
    exponent = exp(-0.5 * (x - mean) ** 2 / variance)
    return coefficient * exponent

# mean is the location of the vehicle
# and variance measures the certainty. Wide variance means estimation has higher uncertainty and vice ver
# the location of the vehicle is estimated using the prior mean and measurement mean

# measurement update equations are responsible for improving the posteriori estimate by using new measurement
def update(prioriMean, prioriVar, measurementMean, measurementVar):
    posterioriMean = (measurementVar * prioriMean + prioriVar * measurementMean) / (prioriVar + measurementVar)
    posterioriVariance = 1 / (1/ measurementVar + 1/ prioriVar)
    return [posterioriMean, posterioriVariance]

# the time update equations are responsible for projecting forward the current estimations to obtain the priori estimations for the next step
# u is the motion
def predict(posterioriMean, posterioriVariance, motionMean, motionVariance):
    prioriMean = posterioriMean + motionMean
    prioriVar = posterioriVariance + motionVariance
    return [prioriMean, prioriVar]

####### TEST THE IDEA  ######

#measurement froms for mu and motions U
measurement = [5.0, 6.0, 7.0, 9.0, 10.0] #location of vehicle
motions = [1.0, 1.0, 2.0, 1.0, 1.0]

#initial parameters
measurementVariance = 4.0
motionVariance = 2.0
mu = 0.
sig = 10000.

for n in range(len(measurement)):
    mean, sigma = update(mean, sigma, measurement[n], measurementVariance)
    print('Update: [{}, {}]'.format(mean, sigma))
    mean, sigma = predict(mean, sigma, motions[n], motionVariance)
    print('Predict: [{}, {}]'.format(mean, sigma))

print('Final: [{}, {}]'.format(mean, sigma)) #mean is the final location of vehicle and variance indicates the uncertainty


