"""
Write a function which takes variable length arguments to receive integers.
Filter out prime numbers and return a list of those prime numbers.
"""

# defining a function prime_list() which takes variable length arguments
# and returns a list of prime numbers
def prime_list(*numbers):
    # creating an empty list for prime numbers
    prime_list = []
    
    for e in numbers:
        i = 2
        while i < e:
            if e%i == 0:
                break
            i += 1
        
        if i == e:
            prime_list.append(e)
            
    return prime_list

# calling prime_list() and printing list of prime numbers
print("Prime Numbers :", prime_list(1,0,2,-1,-34,3,7,9,10,17,19,29,31,36))