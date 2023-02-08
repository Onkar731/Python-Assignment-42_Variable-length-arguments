"""
Write a function which receives length arguments to find greatest element.
It returns the greatest element.
"""

# defining a function find_greatest() which takes variable length argument
# and returns the greatest element
def find_greatest(*numbers):
    return max(numbers)


# finding a greatest number among all variable length arguments 
# and printing them
print("Greatest : %d" %(find_greatest(12,43,23,45,32,12,90,55,78,98)))
print("Greatest : %d" %(find_greatest(12,43,23,45,32,12,900,55,78,98)))
print("Greatest : %d" %(find_greatest(12,-43,23,-23,32,12,90,-5,78,-98)))