#author CJP 11/15/2021
num = list(input("Enter a list of numbers: "))
ans = num.copy()
ans.sort()

if num == ans:
    print("It is sorted. ")
else:
    print("It is not sorted. ")