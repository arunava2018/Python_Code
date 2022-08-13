# cook your dish here
#https://www.geeksforgeeks.org/python-program-to-count-even-and-odd-numbers-in-a-list/
list1=[10, 21, 4, 45, 66, 93, 1]
even_count,odd_count=0,0

for i in list1:
    
    if i%2==0:
       even_count=even_count+1
    else:
        odd_count=odd_count+1
    
print("The count of even number in the ",even_count)
print("The count of odd number in the ",odd_count)