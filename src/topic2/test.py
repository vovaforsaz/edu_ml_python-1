def matricks(file):
    result = file.split(".")
    return result

def create_matrix(dan, all_sentence):
    print("\n")
    for u_word in dan:
        print(u_word, end="\t")
    print("\n")
    for sentence in range(len(all_sentence)):
        tmp_list = all_sentence[sentence].lower()
        for u_word in dan:
            if u_word in tmp_list: #tmp_list.find(u_word) == -1:
                print(0, end="\t\t")
            else:
                print(1, end="\t\t")
        print("\n")
    return None
# file = open("test.txt")
# result = open("test.txt").read()
result = matricks(open("test.txt").read())
print(result)
