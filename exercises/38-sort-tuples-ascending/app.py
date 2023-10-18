def sort_tuples_ascending(items):
    my_list = items.split(" ")
    new_list = []
    name = []
    age = []
    height = []

    for item in my_list:
        new_list.append(item.split(","))

    for x in new_list:
        name.append(x[0])
        age.append(int(x[1]))
        height.append(int(x[2]))

    name.sort()
    age.sort()
    height.sort()

    return tuple(new_list)

# misread the exercise restart it

print(sort_tuples_ascending("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85"))