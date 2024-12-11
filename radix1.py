def radix_sort(arr):
    max_val = max(arr)
    exp = 1 # for reducing the number size  by 1 position from right
    p =1

    while( (max_val//exp) >0):  
        buckets = []
        for i in range(10):
             buckets.append([])  # a list of 10 lists

       # Place each number into the appropriate bucket based on the current digit
        for num in arr:
            digit = (num//exp)%10  # first reduce the number size by 1, then get the last digit
            buckets[digit].append(num)

         #clear the original list
        arr.clear()

         # dump the sorted nums from each bucket in list in sequence(0-9)
        for list in buckets:
              arr.extend(list)
         
        print("pass ",p,":",arr)
        exp = exp*10 
        p+=1;
    return(arr)             
             
a= [22,1,4,34535,23,456,12,786,10,8]
print("Original list :", a)
print("sorted array :", radix_sort(a))