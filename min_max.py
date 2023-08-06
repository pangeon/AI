def min_max(t):
    min = max = t[0]
    for i in range(len(t)):
        if max < t[i]:
            max = t[i]
        if min > t[i]:
            min = t[i]

    return [min, max]

t = input("Enter number values: ").split(",")        
print("range:", min_max(t));
