def string(l):
    return [str(i) for i in l if (type(i) == int or type(i) == float)]
print(string([True, False, [1,2,3], 1, 1.0, 3]))    