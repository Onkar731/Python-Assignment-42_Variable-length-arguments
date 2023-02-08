"""
Write a function which receives variable length arguments to filter odd and even
numbers. Store all odd numbers in a list and all even numbers in another list.
Store both the lists in a tuple and return it.
"""


# defining a function even_odd_lists() which takes variable length arguments
# and returns tuple of list of odd numbers and even numbers
def even_odd_lists(*numbers):
    # creating a tuple of 2 empty list
    t1 = [],[],
    
    for e in numbers:
        if e%2 == 0:
            t1[1].append(e)
        else:
            t1[0].append(e)

    return t1


# calling even_odd_lists() to get tuple of odd even lists
print("Lists are ([odd],[even]):", even_odd_lists(12,43,23,45,32,12,90,55,78,98))
print("Lists are ([odd],[even]):", even_odd_lists(12,43,23,45,32,12,90,55,78,98,4,2,234,21,54,6))
print("Lists are ([odd],[even]):", even_odd_lists(12,43,23,458,233,556,2,1,4,67,44,435,2,321,123))