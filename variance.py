from mean import mean
from sum import sum

t = [1,3,4,2,6,5,3,4,5,2]

def variance(t):
    avg = mean(t)
    t_size = len(t)

    for i in range(t_size):
        t[i] = (t[i] - avg)**2

    return sum(t)/t_size

# print(variance(t))