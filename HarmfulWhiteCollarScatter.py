import matplotlib.pyplot as plt
from collections import Counter

Harm = [7,1,4,6.5,8,8,4,6,8,8,3,2,9,9,8,6,4,6,9,7,5,5,2,2]
Malice = [1,1,2,5,7,7,2,4,8,9,2,1,9,8,8,8,2,8,9,8,6,2,1,1]


c = Counter(zip(Harm,Malice))
# create a list of the sizes, here multiplied by 10 for scale
s = [100*c[(xx,yy)] for xx,yy in zip(Harm, Malice)]

# plot it
plt.scatter(Harm, Malice, s=s, c="salmon")
plt.xlabel("Portrayed Harmfulness")
plt.ylabel("Portrayed Malice")
plt.title("Harmful White Collar Crime Ratings")
plt.show()
