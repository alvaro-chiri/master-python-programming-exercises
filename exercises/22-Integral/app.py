def generate_dict(x):
    my_dict= {}
    for i in range(1, x+1):
        my_dict[i] = i*i
    
    return my_dict

print(generate_dict(8))