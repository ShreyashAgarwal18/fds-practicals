def partition(arr,left,right):
    i=left
    j=right
    pivot = arr[right]
    while i<j:
        while(i<right and arr[i]<pivot):
            i+=1
        while(j>left and arr[j]>=pivot):
            j-=1
        if(i<j):
            arr[i],arr[j] = arr[j], arr[i]
        
    if(arr[i]>pivot):
        arr[i], arr[right] = arr[right], arr[i]
        
    print(arr)
    
    return i

def quicksort(arr,low,high):
    if(low<high):
        pivotpos= partition(arr,low,high)
        quicksort(arr,low,pivotpos-1)
        quicksort(arr,pivotpos+1,high)
        
arr = [3,17,4,65,23]
quicksort(arr,0,4)
    