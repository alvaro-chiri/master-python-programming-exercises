def computed_value(digit):
    a = digit
    aa = int(str(digit)+str(digit))
    aaa = int(str(digit)+str(digit)+str(digit))
    aaaa = int(str(digit)+str(digit)+str(digit)+str(digit))

    return a+aa+aaa+aaaa

print(computed_value(123))