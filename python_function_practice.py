# Write a Python function called max_num()to find the Max of three numbers.

def max_num(*args):
  return max([args])
print(max_num(2,5,9))

# Write a Python function called mult_list()  to multiply all the numbers in a list.

def mult_list(args):
    result=1
    for i in range(0,len(args)):
        result = result*args[i]
    return result    
numbers=[1,2,3,4,5]
print(mult_list(numbers))

# Write a Python function called rev_string() to reverse a string.

def rev_string(my_string):
    if not my_string:
        return ("You must pass in a valid string")
    elif len(my_string)==1:
        return my_string 
    else:
        return rev_string(my_string[1:])+my_string[0]   
print(rev_string("Hello World yet again"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num,start,end):
    if num >=start and num<=end:
        return True
    else:
        return False
print(num_within(15,5,8))

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

from math import factorial
def pascal(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=' ')
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
        print() 
print(pascal(5))