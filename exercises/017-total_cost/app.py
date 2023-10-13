#Complete the function to return the total cost in dollars and cents of N cupcakes. 
#Remember you can return multiple parameters => return a, b
import math
def total_cost(d,c,n):
    dollars = d*n
    cents = c*n
    if cents > 99:
        cents = cents%100
        dollars = dollars + int(math.floor(cents/100))
    return (dollars, cents)
    



#Invoke the function with three intergers: cost(dollars and cents) & number of cupcakes.
print(total_cost(10, 15, 2))
