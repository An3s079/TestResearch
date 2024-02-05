import matplotlib.pyplot as plt
from collections import Counter

Harm_HW = [7,1,4,6.5,8,8,4,6,8,8,3,2,9,9,8,6,4,6,9,7,5,5,2,2]
Malice_HW = [1,1,2,5,7,7,2,4,8,9,2,1,9,8,8,8,2,8,9,8,6,2,1,1]


c1 = Counter(zip(Harm_HW,Malice_HW))
# create a list of the sizes, here multiplied by 10 for scale
s1 = [100*c1[(xx,yy)] for xx,yy in zip(Harm_HW, Malice_HW)]

# plot it
plt.scatter(Harm_HW, Malice_HW, s=s1, c="salmon", alpha= 0.5)

Harm_HS = [3,6,6,7,3,9,8,8,4,6,4,7,8,7,7,5,7,8,8,7,6,5,8,6]
Malice_HS = [2,4,4,6,3,7,6,6,5,4,3,8,8,8,9,5,8,7,7,4,7,7,8,7]


c2 = Counter(zip(Harm_HS,Malice_HS))
# create a list of the sizes, here multiplied by 10 for scale
s2 = [100*c2[(xx,yy)] for xx,yy in zip(Harm_HS,Malice_HS)]

# plot it
plt.scatter(Harm_HS, Malice_HS, s=s2, c="skyblue", alpha= 0.5)


Harm_FW = [8,3,7,5,7,8,7,6.5,1,6,6,7,7.5,8,6.5,7,7,8,4,8,7,6,4,6]
Malice_FW = [8,7,8,7,8,5,8,7,1,8,7,7,6.5,7,7,7,9,6,6,7,8,7,2,7]


c3 = Counter(zip(Harm_FW,Malice_FW))
# create a list of the sizes, here multiplied by 10 for scale
s3 = [100*c3[(xx,yy)] for xx,yy in zip(Harm_FW,Malice_FW)]

# plot it
plt.scatter(Harm_FW, Malice_FW, s=s3, c="mediumaquamarine", alpha= 0.5)

Harm_FS = [5,5,7,5,6,4,5,6,6,7,5,5,3,2,3,7,6,4,7,6,6,7,6.5,7]
Malice_FS = [6,6,8,7,5,6,7,7,7,6,3,6,4,4,2,4,7,6,7,5,8,7,7,8]


c4 = Counter(zip(Harm_FS,Malice_FS))
# create a list of the sizes, here multiplied by 10 for scale
s4 = [100*c4[(xx,yy)] for xx,yy in zip(Harm_FS,Malice_FS)]

# plot it
plt.scatter(Harm_FS, Malice_FS, s=s4, c="mediumslateblue", alpha= 0.5)
plt.legend(["Harmful White Collar Crime" , "Harmful Street Crime", "Financial White Collar Crime", "Financial Street Crime"])
plt.xlabel("Portrayed Harmfulness")
plt.ylabel("Portrayed Malice")
plt.title("Crime Ratings")

plt.show()
