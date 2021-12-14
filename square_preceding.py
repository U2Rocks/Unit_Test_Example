def square_preceding(values):
    if values !=[]:
        temp = values[0]
        values[0] = 0
    for i in range(1, len(values)):
        values[i] = temp ** 2
        temp = values[i]
    return values
