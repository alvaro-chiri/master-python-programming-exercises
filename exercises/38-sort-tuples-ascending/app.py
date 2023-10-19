# def sort_tuples_ascending(tuples):
#     # Split the input string into a list of tuples
#     tuple_strings = tuples.split()
    
#     # Split each tuple string into individual elements and convert to a tuple
#     tuple_list = [tuple(t.split(',')) for t in tuple_strings]
    
#     # Sort the list of tuples based on the specified criteria
#     sorted_list = sorted(tuple_list, key=lambda x: (x[0], x[1], x[2]))
    
#     return sorted_list

from operator import itemgetter

def sort_tuples_ascending(tuples):
    # Split the input string into individual tuples
    tuple_list = tuples.split()
    
    # Split each tuple into its components and create a list of tuples
    tuple_list = [tuple(t.split(",")) for t in tuple_list]
    
    # Sort the list of tuples based on the first, second, and third elements
    sorted_tuples = sorted(tuple_list, key=itemgetter(0, 1, 2))
    
    return sorted_tuples



# Test cases
print(sort_tuples_ascending("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85"))
print(sort_tuples_ascending("Martin,23,30 Tomas,25,27"))