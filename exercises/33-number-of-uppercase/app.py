def letters_and_digits(text):
    uppercase = 0
    lowercase = 0

    for char in text:
        if char.isupper():
            uppercase +=1
        if char.islower():
            lowercase += 1

    return f"UPPER CASE {uppercase} LOWER CASE {lowercase}"

print(letters_and_digits("Hello World! 123"))

#result is UPPER CASE 2 LOWER CASE 8