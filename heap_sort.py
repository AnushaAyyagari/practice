import math
# the first function here is the heap sort function
#we are first checking for the lenght of the array, if the array has only one element then we do nothing and say that there no need for sorting
#if the array has more than one element then we call the function buildheap by passing the array and size of the array as parameters to build a heap.
#once the heap is built we start the extraction phase
#for i in range(size-1,0,-1): here the for loop starts with the bottom most node of the tree(size-1) and continue till the root node denoted by '0' is reached
#and the '-1' is for the decreasing order since we are going from bottom to the top
#arr[0],arr[i]=arr[i],arr[0]  we are taking the maximum element which is present in the root node and replacing it with the bottom most element in the heap by doing this we are removing
# the maximum element from the heap and placing it in an array.
#size = size - 1 we are reducing the size of the heap by element
#we are calling the hapify function and passing the parameters as the array,'0' as the root index and the updated size(as we are removing the maximum element from the heap)
#so that it can perform the comparisions.

#the 2nd function here is the buildheap
#we are giving the array and the initial size of the array to start building a heap
#for i in range(math.floor(size/2-1),-1,-1): when we build a heap we are starting with the last but one level(the parent node) so that we can have child nodes 
#example if we have an array like [12, 11, 13, 5, 6, 7]. we will start building a heap from 3rd element wich in this case will be 13 which will be the penultimate right node
#we do this to build a balanced heap
#the -1 so that we can go upto the root
#the next -1 is to decrese the level by 1 each time.


#the heapify function
# this function will check if there is a left child node and a right child node the left child with be at the (2*root+1)th position and the right child will be at the (2*root+2)th position
#as long as we are withing the array size if the elemnt in the left or the right child is greater than the parent  then swap the elemnts with the greater value
#after Swapping call the heapify function again on the node whose value was swapped.



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
