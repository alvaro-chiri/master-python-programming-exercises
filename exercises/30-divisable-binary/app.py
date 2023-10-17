def divisable_binary(string):
    clean_str = string.split(',')
    new_list = []

    for i in clean_str:

        if int(i, 2) % 5 ==0:
            new_list.append(i)

    return ','.join(new_list)

print(divisable_binary("1111,1000,0101,0000"))