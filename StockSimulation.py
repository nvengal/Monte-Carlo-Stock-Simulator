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

#Calculates value of equity
def calcValue(rate, value):
    value += rate*value
    return value

#Set initial conditions
def initial():
    valueStock = 9000
    valueBond = 1000
    valuePureStock = 10000
    return valueStock,valueBond, valuePureStock

y = 0
yearsPerIteration = 70
totalIterations = 10000
pureStockWins = 0
mixedPortfolioWins = 0
valueStock, valueBond, valuePureStock = initial()

#Run multiple times
while y<totalIterations:
    x = 0
#Calculate change in fund value
    while x<yearsPerIteration:
        stockRate = calcStockRate()
        valueStock = calcValue(stockRate, valueStock)
        valueBond = calcValue(calcBondRate(), valueBond)
        valuePureStock = calcValue(stockRate, valuePureStock)
        x += 1

    #print "Stock value = ", valueStock, " Bond Value = ", valueBond
    #print "Total Mixed = ", valueStock+valueBond
    #print "Pure Stock = ", valuePureStock

    #Compare mixed to pure portfolios and count
    if (valueStock + valueBond) > valuePureStock:
        mixedPortfolioWins += 1
    if (valueStock + valueBond) < valuePureStock:
        pureStockWins += 1
    y += 1
    #Reset portfolios
    valueStock, valueBond, valuePureStock = initial()

print "Years per iteration: ", yearsPerIteration, "Total Iterations: ", totalIterations
print "Mixed portfolios won: ", mixedPortfolioWins
print "Pure stock won: ", pureStockWins
print "Percent mixed wins: ", float(mixedPortfolioWins)/float(totalIterations)*100
