# Author: SCT (AMDG) 12/3/21

total = 0
while True:
    num = int(input("Input a number:"))
    if num == int(-1):
        break
    else:
        total += int(num)
print("The total is {0}".format(total))
