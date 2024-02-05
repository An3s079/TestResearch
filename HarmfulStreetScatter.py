import matplotlib.pyplot as plt
from collections import Counter

Harm = [3,6,6,7,3,9,8,8,4,6,4,7,8,7,7,5,7,8,8,7,6,5,8,6]
Malice = [2,4,4,6,3,7,6,6,5,4,3,8,8,8,9,5,8,7,7,4,7,7,8,7]


c = Counter(zip(Harm,Malice))
# create a list of the sizes, here multiplied by 10 for scale
s = [100*c[(xx,yy)] for xx,yy in zip(Harm,Malice)]

# plot it
plt.scatter(Harm, Malice, s=s, c="skyblue")
plt.xlabel("Portrayed Harmfulness")
plt.ylabel("Portrayed Malice")
plt.title("Harmful Street Crime Ratings")
plt.show()
