# def two_dimensional_array(nList, nElements):
#     rowNum = int(nList)
#     colNum = int(nElements)

#     multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

#     for row in range(rowNum):
#         for col in range(colNum):
#             multilist[row][col] = row*col

#     return multilist


# print(two_dimensional_array(2, 7))


# the below is to practice and to prove I remembered how to do it
def two_dimensional_array(nList, nElement):
    rowNum = int(nList)
    colNum = int(nElement)

    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col] = row*col

    return multilist

print(two_dimensional_array(3,5))