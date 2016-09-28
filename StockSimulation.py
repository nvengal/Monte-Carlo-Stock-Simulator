from StockSimulationFunctions import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


#Initialize
yearsPerIteration = float(60)
totalIterations = float(10000)
meanStockRate = .101 #Average yearly stock return (Default: .101)
stDevStock = .201 #Standard deviation of stock return (Default: .201)
meanBondRate = .056 #Average yearly bond return (Default: .056)
stDevBond = .097 #Standard deviation of bond return (Default: .097)
initialValue = float(10000) #Initial value of portfolio
percentStock = .9 #Percentage of portfolio in stocks

y = 0 #Count for Monte Carlo
pureStockWins = 0
mixedPortfolioWins = 0
rebalancedPortfolioWins = 0
value = initial(initialValue, percentStock)

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
        changeValue(stockRate, bondRate, value) 
        #Rebalance rebalancing portfolio
        value[3], value[4] = rebalance(value[3], value[4], percentStock)
        x += 1

    #Compare mixed to rebalanced to pure portfolios and count
    if (value[0] + value[1]) > value[2] and (value[0] + value[1]) > (value[3] + value[4]):
        mixedPortfolioWins += 1
    if value[2] > (value[0] + value[1]) and value[2] > (value[3] + value[4]):
        pureStockWins += 1
    if (value[3] + value[4]) > value[2] and (value[3] + value[4]) > (value[0] + value[1]):
        rebalancedPortfolioWins += 1

    #Append data for plotting
    iX.append(y)
    mixedY.append(value[0]+value[1])
    pureY.append(value[2])
    rebalY.append(value[3]+value[4])
    
    #Reset portfolios
    value = initial(initialValue, percentStock)
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
print("  Avg growth: ", round((((sum(mixedY)/totalIterations)/initialValue-1)*100), 2), "%")
#print("    Median growth: ", round(((mixedY[int(totalIterations/2)]/initialValue-1)*100), 2), "%")
print("Pure stock won: ", round((pureStockWins/totalIterations*100), 2), "%")
print("  Avg growth: ", round((((sum(pureY)/totalIterations)/initialValue-1)*100), 2), "%")
#print("    Median growth: ", round(((pureY[int(totalIterations/2)]/initialValue-1)*100), 2), "%")
print("Rebalanced portfolio won: ", round((rebalancedPortfolioWins/totalIterations*100), 2), "%")
print("  Avg growth: ", round((((sum(rebalY)/totalIterations)/initialValue-1)*100), 2), "%")
#print("    Median growth: ", round(((rebalY[int(totalIterations/2)]/initialValue-1)*100), 2), "%")

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
