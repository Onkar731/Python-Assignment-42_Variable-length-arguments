"""
Write a function which receives variable length arguments to calculate
average of integers. It returns the average of numbers.
"""

# defining a function avg() which takes variable length arguments
# and returns the average of numbers
def avg(*numbers):
    return sum(numbers)/len(numbers);


# passing multiple numbers to avg() and printing average
print("Average : %.2f" %(avg(12,43,23,45,32,12,90)));
print("Average : %.2f" %(avg(12,43,23,45,32,12,90,55,78,98)));
print("Average : %.2f" %(avg(12,43,23,45,32,12,90,56,44)));