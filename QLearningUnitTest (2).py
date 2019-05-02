import math

def sigmoid(z):
        sig = 1.0 / float(1.0 + math.exp(-z))
        return sig

print(sigmoid(1.5))