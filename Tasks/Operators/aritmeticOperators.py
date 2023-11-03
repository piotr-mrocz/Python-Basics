capital = 5000
rateOfInterest = 0.08
inflationRate = 0.15

returnValue = capital * rateOfInterest
capitalAfterInfaltion = capital * inflationRate

capital = capital + returnValue - capitalAfterInfaltion
print(capital)