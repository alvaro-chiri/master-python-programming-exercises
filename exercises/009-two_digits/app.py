import math #Complete the function to return the tens digit and the ones digit of any interger.
def two_digits(digit):
  tens = math.floor(digit /10)
  ones = digit %10

  return (tens, ones)
   


#Invoke the function with any interger as its argument.
print(two_digits(79))
