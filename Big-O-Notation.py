#Big O Notation is simply a method we use to know the efficiency of algorithms
#  in terms of time or space (memory) when the size of the data we are working on increases.

# Big O Notation is used to measure How runing time or 
# space requirments for your program grow as input size grows .

#Big O notation describes the worst-case scenario for an algorithm’s growth rate

# Big O notation => Order of => Growth rate
# n => The amount of data 


# importance of Big O Notation 
# 1. (time complexity ) time to excuate code .
# 2. (space complexity ) Memory space consumed .

# How to use it ?
# We calculate the relationship between data size n and execution time or memory consumption.
    # If n increases too much, how slow will the code be?
    # If n is small, is the code really fast?


# 1. O(1): constant time 
#It means that time is constant, regardless of the size of the data
#the algorithm runs in the same amount of time regardless of input size.
# Check if the first element of the list is even
def is_first_element_even(numbers):
    return numbers[0] % 2 == 0
# This runs in constant time, O(1), regardless of the length of `numbers`



#2.  o(n) linar time 
# Time increases with the same amount of data .
# the runtime grows linearly with the size of the input.
# Calculate the sum of all elements in a list .
def sum_of_elements(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
# The time complexity is O(n), where `n` is the length of `numbers`.


# 3.  O(n2) : Quadratic Time
# The time increases with the square of the data size (suitable for algorithms with nested loops).
# the runtime grows quadratically as the input size increases.
# Check for duplicates in a list
def has_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
            return False
# The time complexity is $O(n^2)$ due to the nested loops.


# 4. O(log n): Logarithmic Time
# Performance increases more slowly as data size increases (common in binary search).
# the runtime grows logarithmically, which is very efficient for large inputs.
# Binary search to find a target element in a sorted list
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# The time complexity is O(log n), as the input size is halved at each step


# 5. O(n log n) - a mixture of linear and logarithmic
#     Common in some sorting algorithms such as Merge Sort.
# 6. O(2^n) - exponential
# The time increases exponentially as the data increases.
#  It is rarely used because it is very slow with large data.

#Big O	الأداء	مثال
# O(1)	ثابت 	الوصول لعُنصر في قائمة.
# O(n)	خطي	 المرور على كل عناصر القائمة.
# O(n^2)	تربيعي	الحلقات المتداخلة (nested loops).
# O(log n)	لوغاريتمي	البحث الثنائي (Binary Search).
# O(n log n)	خلط بين الخطي واللوغاريتمي	ترتيب مثل Merge Sort.

# what is complexity ? => measure of the efficiency of an algorithm
# Time Complexity => amount of time an algorithm takes to com-plete its execution as 
# a function of the input size
# Space Complexity => amount of memory an algorithm uses during its execution as
#  a function of the input size

