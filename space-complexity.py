# space complexity => measures the amount of memory an algorithm uses relative
# to the input size. This includes all the memory consumed by the input,
# variables, and data structures that the algorithm requires for its execution.


# O(1): Constant Space
# Find the maximum element in a list
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
## The space complexity is O(1) since only a fixed amount of memory is used.


# O(n): Linear Space
# Return a list containing the squares of all elements
def square_elements(numbers):
    squares = []
    for num in numbers:
        squares.append(num ** 2)
    return squares
# The space complexity is O(n), where `n` is the length of `numbers`.


# 1.3.4 Analyzing Complexity: Practical Tips
# When analyzing an algorithm’s time and space complexity, it’s important to:
# • Focus on the dominant term of the complexity expression. For example,
# in a complexity of O(n2 + n), the dominant term is O(n2).
# • Ignore constant factors. For instance, O(2n) simplifies to O(n) because
# Big O focuses on the growth rate.
# • Consider the worst-case scenario to ensure the algorithm performs well
# under all conditions.
