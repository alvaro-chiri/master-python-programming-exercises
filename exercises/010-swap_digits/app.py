import math #Complete the fuction to return the swapped digits of a given two-digit-interger.
def swap_digits(num):
  # Your code here
  tens = math.floor(num/10)
  ones = num%10

  num_str = str(ones)+str(tens)

  result = int(num_str)

  return result
   
#Invoke the function with any two digit interger as its argument
print(swap_digits(30))
