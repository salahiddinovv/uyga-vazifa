import os
os.system("cls")

def min (lst: list):
    element = sorted(lst)[2]
    print(element)

lst = [5,7,6,1,8,7,9,3,2,4,6,7,1,3]
min(lst)