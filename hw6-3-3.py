# author CJP 11/15/2021

numbers = input("Enter a list of 5 numbers seperated by spaces: ")

firstlst = list(numbers)
sorted = firstlst.copy()
sorted.sort()
num = sorted[4:]

total = (int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + int(num[4]))
print(total)