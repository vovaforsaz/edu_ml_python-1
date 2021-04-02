from itertools import combinations_with_replacement

sentence1 = "Socrates likes to watch movies. Mary likes movies too."
sentence2 = "Rene Descartes likes to watch movies. Mary likes movies too."
sentence3 = "Kant also likes to watch football games"
all_sentence = []
all_sentence.append(sentence1)
all_sentence.append(sentence2)
all_sentence.append(sentence3)

dan = ['socrates', 'likes', 'watch', 'movies', 'mary', 'rene', 'descartes', 'kant', 'football', 'games']
print("\n")
for u_word in dan:
    print(u_word, end="\t")
print("\n")
for sentence in range(len(all_sentence)):
    tmp_list = all_sentence[sentence].lower()
    for u_word in dan:
        a = []
        if tmp_list.find(u_word) == -1:
            print(0, end="\t\t")
        else:
            print(1, end="\t\t")
    print("\n")