#Complete the function to return how many hrs and min are displayed on the 24th digital clock.
import math 
def digital_clock(n):
  hour = 0
  if n > 60:
    hour = math.floor(n/60)
  
  minutes = n%60

  return (hour, minutes)

#Invoke the function with any interger (seconds after midnight)
print(digital_clock(150))
