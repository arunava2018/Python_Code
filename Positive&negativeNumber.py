list=[90,-78,45,-64,87,-12]
count_positive=0
count_negative=0
for i in list:
    if i>=0:
        count_positive=count_positive+1
    else:
        count_negative=count_negative+1
print("The positive number count is : ",count_positive)
print("The negative number count is : ",count_negative)


