import numpy as np
x = np.array([3,6,7,8,5,6,4])
y = np.array([7,3,9,2,6,4,7])

k = (np.mean(x*y) - np.mean(x)*np.mean(y)) / (np.mean(x**2) * np.mean(x)**2)
b = np.mean(y) - k*np.mean(x)

print(k, b)

std_k = 1/np.sqrt(len(x)) * np.sqrt((np.mean(y**2)-np.mean(y)**2)/((np.mean(x**2)-np.mean(x)**2))-k**2)
str_b = std_k* np.sqrt(np.mean(x**2)-np.mean(x)**2)

print(std_k, str_b)