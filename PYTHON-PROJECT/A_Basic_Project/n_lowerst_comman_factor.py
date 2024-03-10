import math
def lcm(x,y):
    gcd = math.gcd(x, y)
    return (x * y) // gcd

print(lcm(4, 8)) #

