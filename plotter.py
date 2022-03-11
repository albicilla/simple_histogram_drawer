import numpy as np
import matplotlib.pyplot as plt

INPUT = "InputFile"

data = np.loadtxt(INPUT,dtype=np.uint64,delimiter='\n')
print("Data loaded into memory")

unique_cnt = len(np.unique(data))


print(unique_cnt)
print(data)

# Generate histograms
plt.hist(data,bins=unique_cnt)
plt.savefig("hist.png")
plt.show()
print("Histogram generated")
