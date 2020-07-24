import numpy as np
import matplotlib.pyplot as plt

text = np.read('words.txt')
text = text[:5]
np.savetxt('data.txt', text)
data2 = np.loadtxt('data.txt')
print(data2)