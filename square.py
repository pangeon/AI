from abs import abs

def square(limit, approximation = 0.0001):
    left_limit = 0
    right_limit = limit

    while abs(right_limit - left_limit) > approximation:
        range = abs(left_limit + right_limit) / 2
        if limit < range**2:
            right_limit = range
        else:
            left_limit = range

    return range
