sentence = input()
sentence = sentence.strip()
frequency = {}
words = sentence.split(' ')
words_sorted = sorted(words)

for word in words_sorted:
    if word in frequency:
            frequency[word] += 1
    else:
            frequency[word] = 1

output_list = []

for w in frequency:
       output_list.append(f"{w}:{frequency[w]}")

print(' '.join(output_list))

freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words_sorted = sorted(words)

for w in words_sorted:
    print(f"{w}:{freq[w]}")