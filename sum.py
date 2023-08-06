def sum(t):
    sum = 0

    for i in t:
        sum += int(i)

    return sum

t = input("Enter number values: ").split(",")
print("sum:", sum(t))
