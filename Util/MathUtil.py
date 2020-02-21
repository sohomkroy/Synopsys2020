def clip(input: float, lower_bound: float, upper_bound: float):
    if (input < lower_bound):
        return lower_bound
    elif (input > upper_bound):
        return upper_bound
    else:
        return input
