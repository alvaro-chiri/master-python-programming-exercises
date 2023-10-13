#Complete the function "digits_sum" so that it prints the sum of a three digit number.
def digits_sum(num):
  total = 0
  for i in range(len(str(num))):
    total += int(str(num)[i])
  return total


#Invoke the function with any three-digit-number
#You can try other three-digit numbers if you want
print(digits_sum(123))