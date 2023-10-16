def remove_duplicate_words(listwords):
    s = listwords
    words = [word for word in s.split(" ")]
    return " ".join(sorted(list(set(words))))

print(remove_duplicate_words('blue age blue track'))