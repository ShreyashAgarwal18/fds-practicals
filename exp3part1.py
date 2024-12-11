#linear search
def linearsearch(l,k):
    count = 0
    for i in range(0, len(l)):
        if(l[i]==k):
            count+=1
            print("Total comparison: ", count)
            return("found at: ",i)
        count+=1
    print("total comparisons: ", count)
    return("not found")

def binarysearch(l,k):
    s = 0
    e = len(l)-1
    while(s<=e):
        mid = s + (e-s)//2
        if(l[mid]==k):
            return("found at: ", mid)
        
        elif(l[mid]<k):
            s = mid + 1
            
        elif(l[mid]>k):
            e = mid-1 
            
    return("not found!")

#sentinel search
def sentinel(l,n,k):
    last = l[n-1];
    l[n-1] = k;
    for i in range(n-1):
        if(l[i] == k):
            return True
        
    if (last == k):
        return True
    else:
        return False



n = int(input("enter elements: "))
l = []
for i in range(0,n):
    i = int(input("Enter number: "))
    l.append(i)
k = int(input("Element to Search: "))

print()

print(linearsearch(l,k))

print()

print(binarysearch(l,k))

print(sentinel(l,n,k))


        
