#1st Approach
def combination(L):

    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and i!=k):
                    print(L[i], L[j], L[k])


combination([1,2,3])

#2nd Approach:
from itertools import permutations

comb=permutations([1,2,3],3)
for i in comb:
    print(i)
  