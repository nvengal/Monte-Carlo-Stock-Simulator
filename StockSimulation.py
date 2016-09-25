import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#Calculates random yearly return from the S&P 500
def calcStockRate(mu, sigma):
    #Random value based on a gaussian dist
    stockRate = random.gauss(mu, sigma)
    return stockRate

#Calculates random yearly return from the Total Bond Market
def calcBondRate(mu, sigma):
    #Random value based on a gaussian dist
    stockRate = random.gauss(mu, sigma)
    return stockRate

#Rebalances stock to bond ratio
def rebalance(valueRStock, valueRBond):
    percentStock = .9
    percentBond = 1.0 - percentStock
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
    total = 100000
    percentStock = .9
    valueStock = total * percentStock
    valueBond = total - valueStock
    valuePureStock = total 
    valueRStock = total * percentStock
    valueRBond = total - valueStock
    return valueStock,valueBond, valuePureStock, valueRStock, valueRBond

#Initialize
yearsPerIteration = 70
totalIterations = 10000
meanStockRate = .07 #Average yearly stock return
stDevStock = .15 #Standard deviation of stock return
meanBondRate = .05 #Average yearly bond return
stDevBond = .025 #Standard deviation of bond return

y = 0
pureStockWins = 0
mixedPortfolioWins = 0
rebalancedPortfolioWins = 0
valueStock, valueBond, valuePureStock, valueRStock, valueRBond = initial()

#Plot data initialize
iX = [] #iteration on x-axis
mixedY = [] #mixed portfolio on y-axis
pureY = [] #pure portfolio on y-axis
rebalY = [] #rebalanced portfolio on y-axis

#Run multiple times
while y<totalIterations:
    x = 0
#Calculate change in fund value
    while x<yearsPerIteration:
        stockRate = calcStockRate(meanStockRate, stDevStock)
        bondRate = calcBondRate(meanBondRate, stDevBond)
        valueStock = calcValue(stockRate, valueStock)
        valueBond = calcValue(bondRate, valueBond)
        valuePureStock = calcValue(stockRate, valuePureStock)
        valueRStock = calcValue(stockRate, valueRStock)
        valueRBond = calcValue(bondRate, valueRBond)
        #print ("BEFORE Rebalanced Stock Val = ", valueRStock)
        #print ("BEFORE Rebalanced Bond Val = ", valueRBond) 

        valueRStock, valueRBond = rebalance(valueRStock, valueRBond)
        x += 1
        #print ("AFTER Rebalanced Stock Val = ", valueRStock)
        #print ("AFTER Rebalanced Bond Val = ", valueRBond)

    #print ("Stock value = ", valueStock, " Bond Value = ", valueBond)
    #print ("Total Mixed = ", valueStock+valueBond)
    #print ("Pure Stock = ", valuePureStock)

    #Compare mixed to rebalanced to pure portfolios and count
    if (valueStock + valueBond) > valuePureStock and (valueStock + valueBond) > (valueRStock + valueRBond):
        mixedPortfolioWins += 1
    if valuePureStock > (valueStock + valueBond) and valuePureStock > (valueRStock + valueRBond):
        pureStockWins += 1
    if (valueRStock + valueRBond) > valuePureStock and (valueRStock + valueRBond) > (valueStock + valueBond):
        rebalancedPortfolioWins += 1

    #Append data for plotting
    iX.append(y)
    mixedY.append(valueStock+valueBond)
    pureY.append(valuePureStock)
    rebalY.append(valueRStock+valueRBond)
    
    #Reset portfolios
    valueStock, valueBond, valuePureStock, valueRStock, valueRBond = initial()
    y += 1

#Summary
print("Years per iteration: ", yearsPerIteration, "Total Iterations: ", totalIterations)
print("Mean yearly stock return: ", meanStockRate, "Stock standard dev: ", stDevStock)
print("Mean yearly bond return: ", meanBondRate, "Bond standard dev: ", stDevBond)
print("Mixed portfolio won: ", mixedPortfolioWins)
print("Pure stock won: ", pureStockWins)
print("Rebalanced portfolio won: ", rebalancedPortfolioWins) 
print("Percent rebalanced wins: ", float(rebalancedPortfolioWins)/float(totalIterations)*100)

#Plot
mixedY.sort()
pureY.sort()
rebalY.sort()
plt.plot(iX, mixedY, color='red', label='Mixed Portfolio')
plt.plot(iX, pureY, color='blue', label='Pure Stock Portfolio')
plt.plot(iX, rebalY, color='green', label='Rebalanced Portfolio')
##plt.scatter(iX, mixedY, color='red', label='Mixed Portfolio')
##plt.scatter(iX, pureY, color='blue', label='Pure Stock Portfolio')
##plt.scatter(iX, rebalY, color='green', label='Rebalanced Portfolio')
plt.xlabel("Iteration")
plt.ylabel("Portfolio Value")
red_patch = mpatches.Patch(color='red', label='Mixed Portfolio')
blue_patch = mpatches.Patch(color='blue', label='Pure Stock Portfolio')
green_patch = mpatches.Patch(color='green', label='Rebalanced Portfolio')
plt.legend()
plt.show()
