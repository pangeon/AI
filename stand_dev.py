from square import square
from variance import variance

t = [1,3,4,2,6,5,3,4,5,2]

def stand_dev(variance):
    return square(variance)

print(round(stand_dev(variance(t)), 4))