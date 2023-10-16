def sequence_of_words(words):
    wordlist = words.split(",")

    sortedList = sorted(wordlist)

    return ','.join(sortedList)

print(sequence_of_words('without,hello,bag,world'))