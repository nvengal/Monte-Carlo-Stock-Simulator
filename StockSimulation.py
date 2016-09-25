import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
def calcValue(rate, value):
    value += rate*value
    return value

#Set initial conditions
def initial(total, percentStock):
    valueStock = total * percentStock
    valueBond = total - valueStock
    valuePureStock = total 
    valueRStock = total * percentStock
    valueRBond = total - valueStock
    return valueStock,valueBond, valuePureStock, valueRStock, valueRBond

#Initialize
yearsPerIteration = float(60)
totalIterations = float(10000)
meanStockRate = .101 #Average yearly stock return
stDevStock = .201 #Standard deviation of stock return
meanBondRate = .056 #Average yearly bond return
stDevBond = .097 #Standard deviation of bond return
total = float(100000) #Initial value of portfolio
percentStock = .9 #Percentage of portfolio in stocks

y = 0
pureStockWins = 0
mixedPortfolioWins = 0
rebalancedPortfolioWins = 0
valueStock, valueBond, valuePureStock, valueRStock, valueRBond = initial(total, percentStock)

#Plot data initialize
iX = [] #iteration on x-axis
mixedY = [] #mixed portfolio on y-axis
pureY = [] #pure portfolio on y-axis
rebalY = [] #rebalanced portfolio on y-axis

#Run multiple times
while y<totalIterations:
    x = 0
    #Calculate yearly change in fund value
    while x<yearsPerIteration:
        stockRate = calcRate(meanStockRate, stDevStock)
        bondRate = calcRate(meanBondRate, stDevBond)
        valueStock = calcValue(stockRate, valueStock)
        valueBond = calcValue(bondRate, valueBond)
        valuePureStock = calcValue(stockRate, valuePureStock)
        valueRStock = calcValue(stockRate, valueRStock)
        valueRBond = calcValue(bondRate, valueRBond)
##        print ("BEFORE Rebalanced Stock Val = ", valueRStock)
##        print ("BEFORE Rebalanced Bond Val = ", valueRBond) 
        #Rebalance rebalancing portfolio
        valueRStock, valueRBond = rebalance(valueRStock, valueRBond, percentStock)
        x += 1
##        print ("AFTER Rebalanced Stock Val = ", valueRStock)
##        print ("AFTER Rebalanced Bond Val = ", valueRBond)
##
##    print ("Stock value = ", valueStock, " Bond Value = ", valueBond)
##    print ("Total Mixed = ", valueStock+valueBond)
##    print ("Pure Stock = ", valuePureStock)

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
    valueStock, valueBond, valuePureStock, valueRStock, valueRBond = initial(total, percentStock)
    y += 1

#Sort for line plot and median calc COMMENT OUT for scatter plot
mixedY.sort()
pureY.sort()
rebalY.sort()

#Summary
print("Years per iteration: ", yearsPerIteration, "Total Iterations: ", totalIterations)
print("Mean yearly stock return: ", meanStockRate, "Stock standard dev: ", stDevStock)
print("Mean yearly bond return: ", meanBondRate, "Bond standard dev: ", stDevBond)
print("Mixed portfolio won: ", round((mixedPortfolioWins/totalIterations*100), 2), "%")
print("  Avg growth: ", round((((sum(mixedY)/totalIterations)/total-1)*100), 2), "%")
#print("    Median growth: ", round(((mixedY[int(totalIterations/2)]/total-1)*100), 2), "%")
print("Pure stock won: ", round((pureStockWins/totalIterations*100), 2), "%")
print("  Avg growth: ", round((((sum(pureY)/totalIterations)/total-1)*100), 2), "%")
#print("    Median growth: ", round(((pureY[int(totalIterations/2)]/total-1)*100), 2), "%")
print("Rebalanced portfolio won: ", round((rebalancedPortfolioWins/totalIterations*100), 2), "%")
print("  Avg growth: ", round((((sum(rebalY)/totalIterations)/total-1)*100), 2), "%")
#print("    Median growth: ", round(((rebalY[int(totalIterations/2)]/total-1)*100), 2), "%")

#Plot
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
