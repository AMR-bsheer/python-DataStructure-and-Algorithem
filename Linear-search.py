# Summary
#  Algorithms
#  Execution Time
#  Asymptotic Analysis
#  Linear Search
#  Big-O
#  Evaluating Python Code
#  Binary Search
#  Amortized Analysis
#  Sorting
#  Bubble Sort
#  Selection Sort
#  Insertion Sort


# linear search
def linear_search ( arr , n , target ) :
    i = 0
    for i in range ( i , n ) :
        if ( arr [i] == target ) :
            return i
    return -1

arr = [ 1 , 10 , 30 , 15 ] 
target = 30
n = len ( arr )
print ( target , " is present at index " , linear_search ( arr , n , target ) )

