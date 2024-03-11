# num = int(input("Enter any number to check prime of not:"))

# flag = False

# if num == 1:
#     print(num, "is not a prime number")

# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break

#     if flag:
#         print(num, "is not prime number")

#     else:
#         print(num, "is a prime number")


import math
def is_prime(n):
    if n < 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        
    return True

print(is_prime(6))
print(is_prime(5))
print(is_prime(9))