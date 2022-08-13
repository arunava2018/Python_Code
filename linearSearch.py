def linearSearch(arr,curr_index,x):
    if(curr_index==-1):
        return -1
    
    if arr[curr_index]==x:
        return curr_index
    return linearSearch(arr, curr_index-1, x)


 