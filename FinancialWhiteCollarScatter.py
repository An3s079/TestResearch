import matplotlib.pyplot as plt
from collections import Counter

Harm = [8,3,7,5,7,8,7,6.5,1,6,6,7,7.5,8,6.5,7,7,8,4,8,7,6,4,6]
Malice = [8,7,8,7,8,5,8,7,1,8,7,7,6.5,7,7,7,9,6,6,7,8,7,2,7]


c = Counter(zip(Harm,Malice))
# create a list of the sizes, here multiplied by 10 for scale
s = [100*c[(xx,yy)] for xx,yy in zip(Harm,Malice)]

# plot it
plt.scatter(Harm, Malice, s=s, c="mediumaquamarine")
plt.xlabel("Portrayed Harmfulness")
plt.ylabel("Portrayed Malice")
plt.title("Financial Street Crime Ratings")
plt.show()
