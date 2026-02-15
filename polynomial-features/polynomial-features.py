def polynomial_features(values, degree):
    # Write code here
    features = []
    for x in values:
        row = [float(x ** y) for y in range(degree + 1)]
        features.append(row)
    return features
'''
values = [2,3]
degree = 2

polynomial_features(values, degree)
'''