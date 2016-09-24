import random

#Calculates random yearly return from the S&P 500
def calcStockRate():
    #Mean Return
    mu = .07
    #Standard Deviation
    sigma = .15
    #Random value based on a gaussian dist
    stockRate = random.gauss(mu, sigma)
    return stockRate

#Calculates random yearly return from the Total Bond Market
def calcBondRate():
    #Mean Return
    mu = .05
    #Standard Deviation
    sigma = .025
    #Random value based on a gaussian dist
    stockRate = random.gauss(mu, sigma)
    return stockRate

#Rebalances stock to bond ratio
def rebalance(valueRStock, valueRBond):
    percentStock = .9
    percentBond = .1
    total = valueRStock + valueRBond
    valueRStock = total * percentStock
    valueRBond = total * percentBond
    return valueRStock, valueRBond

#Calculates value of equity
def calcValue(rate, value):
    value += rate*value
    return value

#Set initial conditions
def initial():
    valueStock = 9000
    valueBond = 1000
    valuePureStock = 10000
    valueRStock = 9000
    valueRBond = 1000
    return valueStock,valueBond, valuePureStock, valueRStock, valueRBond

#Initialize
y = 0
yearsPerIteration = 70
totalIterations = 10000
pureStockWins = 0
mixedPortfolioWins = 0
rebalancedPortfolioWins = 0
valueStock, valueBond, valuePureStock, valueRStock, valueRBond = initial()

#Run multiple times
while y<totalIterations:
    x = 0
#Calculate change in fund value
    while x<yearsPerIteration:
        stockRate = calcStockRate()
        bondRate = calcBondRate()
        valueStock = calcValue(stockRate, valueStock)
        valueBond = calcValue(bondRate, valueBond)
        valuePureStock = calcValue(stockRate, valuePureStock)
        valueRStock = calcValue(stockRate, valueRStock)
        valueRBond = calcValue(bondRate, valueRBond)
        #print "BEFORE Rebalanced Stock Val = ", valueRStock
        #print "BEFORE Rebalanced Bond Val = ", valueRBond 
        valueRStock, valueRBond = rebalance(valueRStock, valueRBond)
        x += 1

        #print "AFTER Rebalanced Stock Val = ", valueRStock
        #print "AFTER Rebalanced Bond Val = ", valueRBond
    #print "Stock value = ", valueStock, " Bond Value = ", valueBond
    #print "Total Mixed = ", valueStock+valueBond
    #print "Pure Stock = ", valuePureStock

    #Compare mixed to rebalanced to pure portfolios and count
    if (valueStock + valueBond) > valuePureStock and (valueStock + valueBond) > (valueRStock + valueRBond):
        mixedPortfolioWins += 1
    if valuePureStock > (valueStock + valueBond) and valuePureStock > (valueRStock + valueRBond):
        pureStockWins += 1
    if (valueRStock + valueRBond) > valuePureStock and (valueRStock + valueRBond) > (valueStock + valueBond):
        rebalancedPortfolioWins += 1
    y += 1
    #Reset portfolios
    valueStock, valueBond, valuePureStock, valueRStock, valueRBond = initial()

print "Years per iteration: ", yearsPerIteration, "Total Iterations: ", totalIterations
print "Mixed portfolio won: ", mixedPortfolioWins
print "Pure stock won: ", pureStockWins
print "Rebalanced portfolio won: ", rebalancedPortfolioWins 
print "Percent rebalanced wins: ", float(rebalancedPortfolioWins)/float(totalIterations)*100
