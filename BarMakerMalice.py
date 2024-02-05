import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import statistics

financialStreet = [6,6,8,7,5,6,7,7,7,6,3,6,4,4,2,4,7,6,7,5,8,7,7,8]

financialWhiteCollar = [8,7,8,7,8,5,8,7,1,8,7,7,6.5,7,7,7,9,6,6,7,8,7,2,7]

harmfulStreet= [2,4,4,6,3,7,6,6,5,4,3,8,8,8,9,5,8,7,7,4,7,7,8,7]

harmfulWhiteCollar = [1,1,2,5,7,7,2,4,8,9,2,1,9,8,8,8,2,8,9,8,6,2,1,1]

Data = {'Harmful White Collar':harmfulWhiteCollar, 
        'Harmful Street':harmfulStreet, 
        "Financial White Collar":financialWhiteCollar,
        "Financial Street":financialStreet}
type = list(Data.keys())
val = list(Data.values())
fig = plt.figure(figsize = (10, 10))

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, round(statistics.mean(y[i]), 2), round(statistics.mean(y[i]), 2), ha = 'center', bbox=dict(facecolor='red', alpha=0.8))
        plt.text(i, statistics.mean(y[i]) + statistics.stdev(y[i]) + 0.1, round(statistics.mean(y[i]) + statistics.stdev(y[i]), 2), ha = 'center')
        plt.text(i, statistics.mean(y[i]) - statistics.stdev(y[i]) - 0.2, round(statistics.mean(y[i]) - statistics.stdev(y[i]) - 0.2, 2), ha = 'center')

# creating the bar plot
plt.bar(type[0], statistics.mean(val[0]), color ='salmon', width = 0.5)
plt.errorbar(type[0], statistics.mean(val[0]), statistics.stdev(harmfulWhiteCollar), fmt='.', color='Black', elinewidth=2,
             capthick=2,errorevery=1, alpha=0.5, ms=4, capsize = 15)

plt.bar(type[1], statistics.mean(val[1]), color ='skyblue', width = 0.5) 
plt.errorbar(type[1], statistics.mean(val[1]), statistics.stdev(harmfulStreet), fmt='.', color='Black', elinewidth=2,
             capthick=2,errorevery=1, alpha=0.5, ms=4, capsize = 15)

plt.bar(type[2], statistics.mean(val[2]), color ='mediumslateblue', width = 0.5) 
plt.errorbar(type[2], statistics.mean(val[2]), statistics.stdev(financialWhiteCollar), fmt='.', color='Black', elinewidth=2,
             capthick=2,errorevery=1, alpha=0.5, ms=4, capsize = 15)


plt.bar(type[3], statistics.mean(val[3]), color ='mediumaquamarine', width = 0.5) 
plt.errorbar(type[3], statistics.mean(val[3]), statistics.stdev(financialStreet), fmt='.', color='Black', elinewidth=2,
             capthick=2,errorevery=1, alpha=0.5, ms=4, capsize = 15)

addlabels(type, val)

plt.yticks(np.arange(0, 11, 1))
plt.xlabel("Crime Type")
plt.ylabel("Average Portrayed Malice")
plt.title("Portrayed Malice of Crime Type")
plt.show()

