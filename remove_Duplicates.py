list1=[1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
duplicate=[]

for i in list1:

    n=list1.count(i)
    if n>1:
        if duplicate.count(i) == 0:  # condition to check
 
            duplicate.append(i)
print(duplicate)