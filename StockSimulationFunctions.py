import random

#Calculates random yearly return of equity
def calcRate(mu, sigma):
    #Random value based on a gaussian dist
    rate = random.gauss(mu, sigma)
    return rate

#Rebalances stock to bond ratio
def rebalance(valueRStock, valueRBond, percentStock):
    percentBond = 1.0 - percentStock
    total = valueRStock + valueRBond
    valueRStock = total * percentStock
    valueRBond = total * percentBond
    return valueRStock, valueRBond

#Calculates value of equity
def calcValue(rate, currentValue):
    currentValue += rate*currentValue
    return currentValue

#Set initial conditions
def initial(total, percentStock):
    value = []
    value.append(total * percentStock) #value[0] mixed stock
    value.append(total - value[0]) #value[1] mixed bond
    value.append(total) #value[2] pure stock
    value.append(total * percentStock) #value[3] rebalanced stock
    value.append(total - value[3]) #value[4] rebalanced bond
    return value

#Calculate yearly changes in value
def changeValue(stockRate, bondRate, value):
    value[0] = calcValue(stockRate, value[0])
    value[1] = calcValue(bondRate, value[1])
    value[2] = calcValue(stockRate, value[2])
    value[3] = calcValue(stockRate, value[3])
    value[4] = calcValue(bondRate, value[4])
    return value
