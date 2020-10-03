# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    '''For each element in the list, bubble elements towards the right by swapping them
       with their neighbor'''
    #Keep looping from beginning of list to end until all elements are sorted (swapped flag)
    #Start flag as true
    swapped = True
    while swapped:
        #set swapped to false (it will be corrected to true in the for loop
        #unless the array is sorted)
        #Loop through the elements of the list
        for i in range(len(arr-1)):
            #If an element is greater than the next element, swap them
            if arr[i] > arr[i+1]:
                #swap
                #save temporary copy of left element
                temp = arr[i]
                #replace left element with right element
                arr[i] = arr[i+1]
                #replace right element with temporary copy of left element
                arr[i+1] = temp
                #set swapped flag to true so outer loop can look for other
                #elements that need to be swapped
                swapped = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
