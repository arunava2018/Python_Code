#1st Method
list=[12,34,56,78,89]
for i in list:
    if(i==56):
      print("Yes the number is exist")


#2nd Method

list1=[78,90,87,34]
count=list1.count(34)
if count>0:
    print("Exist")
else:
    print("Not Exist")


#3rd Method

list2=[90,45,67,68]
if (67 in list2):
    print("Element exist :")