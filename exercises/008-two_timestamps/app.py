#Complete the funtion to compute how many seconds passed between the two timestamp.
def two_timestamp(hr1,min1,sec1,hr2,min2,sec2):
    first_time = (hr1*60*60)+(min1*60)+sec1
    second_time =(hr2*60*60)+(min2*60)+sec2
    
    return second_time-first_time


#Invoke the fuction and pass two timestamps(6 intergers) as its argument.
print(two_timestamp(1,1,1,2,2,2))