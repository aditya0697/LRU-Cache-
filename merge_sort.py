#function of merge
def merge(arr, first, middle, last):
    n1 = middle - first + 1
    n2 = last - middle
    left_array = [0]*n1
    right_array = [0]*n2
    for i in range(n1):
        left_array[i] = arr[first+i]
    for i in range(n2):
        right_array[i] = arr[middle+1+i]
    l_ptr = 0
    r_ptr = 0
    i=first
    while(i != last+1):
        if(left_array[l_ptr] < right_array[r_ptr]):
            arr[i] = left_array[l_ptr]
            l_ptr = l_ptr+ 1
            i = i + 1
            if(l_ptr >= n1):
                while (i != last+1) :
                    arr[i] = right_array[r_ptr]
                    i= i+1
                    r_ptr = r_ptr + 1
        else:
             arr[i] = right_array[r_ptr]
             r_ptr = r_ptr+ 1
             i = i + 1
             if(r_ptr >= n2):
                 #i= i+1
                 while i != last+1 :
                     arr[i] = left_array[l_ptr]
                     i= i+1
                     l_ptr = l_ptr + 1
#function of merge_sort
def merge_sort(arr, first, last):
    if first < last :
        middle = int((first + (last-1))/2)
        #print("first ",first, " last ",last," middle ",middle)
        merge_sort(arr, first, middle)
        merge_sort(arr, middle+1, last)
        merge(arr, first, middle, last)
#Main function
arr = [ 5,6,4,3,90,8,7,1,2,8,7,9,0]
print("length of arr ",len(arr))
print(arr)
merge_sort(arr, 0, len(arr)-1)
print(arr)
