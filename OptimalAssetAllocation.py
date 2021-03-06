from StockSimulationFunctions import *

#Initialize
initialValue = float(input("What is your initial investment? $"))
timePeriod = int(input("How many years do you want to invest for? "))
numberOfIterations = 10000 #Number of Monte Carlo Iterations
meanStockRate = .101 #Average yearly stock return (Default: .101)
stDevStock = .201 #Standard deviation of stock return (Default: .201)
meanBondRate = .056 #Average yearly bond return (Default: .056)
stDevBond = .097 #Standard deviation of bond return (Default: .097)

bestPortfolioSuccess = 0
bestPercent = 0
portfolioType = ""

bestReturns = []

print("Calculating...")
for percentStock in range(101): #Simulate percentages from 0-100
    fixedPortfolioSuccess = 0
    rebalPortfolioSuccess = 0
    percentStock = float(percentStock)/100.0
    currentReturns = []
    
    for iteration in range(0, numberOfIterations): #Monte Carlo iterations
        value = initial(initialValue, percentStock)

        for year in range(0, timePeriod): #Years per iteration
            stockRate = calcRate(meanStockRate, stDevStock)
            bondRate = calcRate(meanBondRate, stDevBond)
            value = changeValue(stockRate, bondRate, value) #Update portfolio value
            value[3], value[4] = rebalance(value[3], value[4], percentStock) #Rebalance rebalancing portfolio
            
        #Update counters for portfolio success
        if (value[0]+value[1])>=initialValue:
            fixedPortfolioSuccess += 1
        if (value[3]+value[4])>=initialValue:
            rebalPortfolioSuccess += 1

        #Append rebalanced portfolio returns to list
        #Assumes rebalanced portfolio is >= fixed portfolio
        currentReturns.append(value[3]+value[4])

    #Record best portfolio
    if fixedPortfolioSuccess>=rebalPortfolioSuccess:
        if fixedPortfolioSuccess>bestPortfolioSuccess:
            bestPortfolioSuccess = fixedPortfolioSuccess
            bestPercent = percentStock
            portfolioType = "Fixed"
            bestReturns = currentReturns
    else:
        if rebalPortfolioSuccess>bestPortfolioSuccess:
            bestPortfolioSuccess = rebalPortfolioSuccess
            bestPercent = percentStock
            portfolioType = "Rebalanced"
            bestReturns = currentReturns
##    print("Fixed Success:", fixedPortfolioSuccess, "Rebal Success:",
##          rebalPortfolioSuccess)
##    print("Best Success:", bestPortfolioSuccess, "Best Percent:", bestPercent)

#Summarize Results
bestReturns.sort()
avgReturn = round((sum(bestReturns)/numberOfIterations/initialValue-1)*100,2)
quartile = int(numberOfIterations/4)
avgBottomQuartile = sum(bestReturns[0:quartile])/quartile
avgTopQuartile = sum(bestReturns[3*quartile:numberOfIterations])/quartile
returnBottomQuartile = round((avgBottomQuartile/initialValue-1)*100,2)
returnTopQuartile = round((avgTopQuartile/initialValue-1)*100,2)
print("Time Frame: ", timePeriod, "Years, Initial Investment: $", initialValue)
print("Best Portfolio Allocation: ", round(100*bestPercent, 2), "% Stocks/",
      round(100*(1-bestPercent), 2), "% Bonds")
print("Best Portfolio Type: ", portfolioType)
print("Break even or better: ", round((float(bestPortfolioSuccess)/
      numberOfIterations)*100, 2), "% chance")
print("Worst: $", round(bestReturns[0],2), "Best: $",
      round(bestReturns[numberOfIterations-1],2))
print("Average return: ", avgReturn, "%")
print("Avg return (bottom quartile): ", returnBottomQuartile, "%")
print("Avg return (top quartile): ", returnTopQuartile, "%")


