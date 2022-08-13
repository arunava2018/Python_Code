def binarySearch(arr,low,high,x):

    if high>=low:
        mid=(high+low)//2

        if arr[mid]==x:
            return mid;
        elif mid>x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid+1, high, x)

    else:
        return -1

arr=[1,2,3,4,5,6,7,8]
n=len(arr)
result=binarySearch(arr, 0, n-1, 4)
if(result!=-1):
    print("The element is present ")
else:
    print("The element is not present : ")    