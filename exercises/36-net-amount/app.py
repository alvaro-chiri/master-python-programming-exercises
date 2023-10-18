def net_amount(text):
    arr = text.split(' ')
    total = 0
    for i in range(0, len(arr), 2):
        if arr[i] == 'D':
            total += int(arr[i+1])
        if arr[i] == 'W':
            total -= int(arr[i+1])
    return total

print(net_amount('D 300 D 300 W 200 D 100'))