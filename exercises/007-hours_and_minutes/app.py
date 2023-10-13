import math
#Complete the function to calculate how many hours and minutes are passed since midnight.
def hours_minutes(secs):
  secs_to_minute = secs/60
  minutes_to_hours = math.floor(secs_to_minute/60)
  remaining_minutes = int(secs_to_minute%60)
  
  return (minutes_to_hours, remaining_minutes)

#Invoke the funtion and pass any interger as its argument.
print(hours_minutes(3900))