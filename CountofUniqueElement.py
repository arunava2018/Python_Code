#1st method
list=[1,1,1,2,2,3,4,4,5,6,6,6,7,8,9,9,9]
empty_list=[]
count=0
for i in list:
    if i not in empty_list:
        count=count+1
        list.append(i)
print(count)

#2nd Method
input_list = [1, 2, 2, 5, 8, 4, 4, 8]

# converting our list to set
new_set = set(input_list)
print("No of unique items in the list are:", len(new_set))
