import math








def heapsort(arr):
    size=len(arr)
    #buildheap(arr,size)
    print(size)
    if size<=1:
        print("there is no need to sort")
    else:
        buildheap(arr,size)
        print(arr)
        for i in range(size-1,0,-1):
            print('Calling heapify here first')
            arr[0],arr[i]=arr[i],arr[0]
            size = size - 1
            heapify(arr, 0, size)

def buildheap(arr,size):
    #size=len(arr)
    #print('hi this is build heap')
    for i in range(math.floor(size/2-1),-1,-1):
        print(arr[i])
        heapify(arr,i, size)
        

def heapify(arr,root, size):
    #print('hiya ')
    #arr is the array
    #size is the number of elements in the heap(size of the heap)
    #root is the assumed root of the heap
    lchild=2*root+1
    rchild=2*root+2
    max_value=root
    print('the root is',arr[root])
    if lchild<size:
        print('left child is',arr[lchild])
    if rchild<size:
        print('right child is',arr[rchild])
    if max_value<size:
        print('the jmax_valueis',arr[max_value])
    if ((lchild<size) and (arr[max_value]<arr[lchild])):       
        max_value=lchild      
    if ((rchild<size) and (arr[max_value]<arr[rchild])):
        max_value=rchild
    
    if (max_value!=root):
        #print(arr[max_value])
        arr[root],arr[max_value]=arr[max_value],arr[root]
        heapify(arr,max_value, size)
    
    
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)

n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])
