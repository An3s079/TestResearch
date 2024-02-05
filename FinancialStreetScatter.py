import matplotlib.pyplot as plt
from collections import Counter

Harm = [5,5,7,5,6,4,5,6,6,7,5,5,3,2,3,7,6,4,7,6,6,7,6.5,7]
Malice = [6,6,8,7,5,6,7,7,7,6,3,6,4,4,2,4,7,6,7,5,8,7,7,8]


c = Counter(zip(Harm,Malice))
# create a list of the sizes, here multiplied by 10 for scale
s = [100*c[(xx,yy)] for xx,yy in zip(Harm,Malice)]

# plot it
plt.scatter(Harm, Malice, s=s, c="mediumslateblue")
plt.xlabel("Portrayed Harmfulness")
plt.ylabel("Portrayed Malice")
plt.title("Financial White Collar Crime Ratings")
plt.show()
