# Author: SCT (AMDG) 12/1/21
def sum(num):
    total = 0
    for value in range(int(num)+1):
        total += value
    return total


number = input("Input a number:")
print(sum(number))
