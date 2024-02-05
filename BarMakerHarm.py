import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import statistics

financialStreet = [5,5,7,5,6,4,5,6,6,7,5,5,3,2,3,7,6,4,7,6,6,7,6.5,7]

financialWhiteCollar = [8,3,7,5,7,8,7,6.5,1,6,6,7,7.5,8,6.5,7,7,8,4,8,7,6,4,6]

harmfulStreet = [3,6,6,7,3,9,8,8,4,6,4,7,8,7,7,5,7,8,8,7,6,5,8,6]

harmfulWhiteCollar = [7,1,4,6.5,8,8,4,6,8,8,3,2,9,9,8,6,4,6,9,7,5,5,2,2]

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
plt.ylabel("Average Portrayed Harmfulness")
plt.title("Portrayed Harmfulness of Crime Type")
plt.show()

