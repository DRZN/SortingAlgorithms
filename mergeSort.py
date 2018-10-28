def mergeSort(arr1,arr2):

    # combining two arrays to compare the values for sorting
    both_arrays=arr1+arr2
    # pointer at the start of the first Array
    pointer1=0
    # pointer at the start of the second array
    pointer2=len(arr1)
    # the array that will be returned
    ret=[0]*(len(arr1)+len(arr2))
    i=0
    
    # traversing through the array and comparing array values at both
    # the pointers only. (since both the arrays are already sorted among them)
    # Here we are merging the two sorted arrays 
    while(pointer2<len(both_arrays) and pointer1<len(arr1)):
        
        if(both_arrays[pointer1]>both_arrays[pointer2]):
            ret[i]=both_arrays[pointer2]
            pointer2+=1  
            if(pointer2==len(both_arrays)):
                ret[i+1:]=both_arrays[pointer1:len(arr1)]
        else:
            ret[i]=both_arrays[pointer1]
            pointer1+=1   
            if(pointer1==len(arr1)):
                ret[i+1:]=both_arrays[pointer2:len(both_arrays)]
        i+=1
        
    if(len(arr1)==0):
        ret=arr2
    if(len(arr2)==0):
        ret=arr1
    return ret

# step tells you how many numbers will be compared at a given time
# by the mergeSort function.
step=2
while((step/2) < len(array)):
    for i in range(0,len(array)-1,step):
        # Size tells you the size of the arrays
        size=step/2    
#         print "Array 1 ",array[i:i+size], "Array 2 ", array[i+size:i+2*size]
        answer=mergeSort(array[i:i+size],array[i+size:i+2*size])
#         print "Sorted array is ", answer
        array[i:i+step]=answer
        
    step=step*2
    
print "sorted array is ", array