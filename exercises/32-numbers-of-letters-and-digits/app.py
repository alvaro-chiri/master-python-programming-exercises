def letters_and_digits(text):
    letters = 0
    digits = 0

    for char in text:
        if char.isalpha():
            letters +=1
        if char.isdigit():
            digits += 1

    return f"LETTERS {letters} DIGITS {digits}"

print(letters_and_digits("hello world! 123"))