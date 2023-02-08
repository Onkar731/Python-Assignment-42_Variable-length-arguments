"""
Wirte a function which takes variable length arguments to receive strings.
Return the list of max length string or strings if multiple strings have 
the same length.
"""


# defining a function list_max_length_string() which takes variable length
# arguments and returns the list of max length string
def list_max_length_string(*strings):
    # creating an empty list of strings
    max_len_string = []
    length = 0
    count = 0
    string = " "
        
    for e in strings:
        if len(e) > length:
            length = len(e)
            string = e
            count += 1
    
    if count == 1:
        return list(strings)
    else:
        max_len_string.append(string)
        return max_len_string
    


# calling list_max_length_strings() and printing max length strings list
print("Max length strings :", list_max_length_string("Onkar", "Yogesh", "Nikhilkumar", "Kaivalya", "Raj"))
print("Max length strings :", list_max_length_string("Onkar", "Onkar", "Onkar", "Onkar", "Onkar"))
