start = 1000
mylist = []

while start < 3000:
    startstr = [char for char in str(start)]

    if int(startstr[0]) % 2 == 0 and int(startstr[1]) % 2 == 0 and int(startstr[2]) % 2 == 0 and int(startstr[3]) % 2 == 0:
        mylist.append(str(start))

    start += 1

result = ",".join(mylist)

print(result)