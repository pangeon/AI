def mean(t):
    sum = 0
    n = 0

    for i in t:
        sum += int(i)
        n += 1

    return sum / n

t = input("Enter number values: ").split(",")
print("mean:", mean(t))
