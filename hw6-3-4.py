#author CJP 11/15/21

firstlst = input("Enter a list of numbers or letters seperated by spaces. ")

x = input("Do you want to find the middle or the end? ")

secondlist = firstlst.split()
ans = len(secondlist) - 1

if x == "middle":
    print(secondlist[1:ans])
elif x == "end":
    print(secondlist[:1] + secondlist[ans:])