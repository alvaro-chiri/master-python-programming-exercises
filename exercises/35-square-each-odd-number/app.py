text = input()

my_list = text.split(',')
new_list =[]

for digit in my_list:
    integer = int(digit)

    if integer %2 != 0:
        new_list.append(digit)


print(','.join(new_list))