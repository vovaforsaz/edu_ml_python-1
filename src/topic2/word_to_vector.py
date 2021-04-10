"""
Why word vectors?

Word Embedding is a language modeling technique used for mapping words to vectors of real numbers.
It represents words or phrases in vector space with several dimensions.

Poetry is, at its core, the art of identifying and manipulating linguistic similarity.
similarity and simple linear algebra

@see https://www.baeldung.com/cs/convert-word-to-vector

TFFDF
PMI
Word Embeddings (CBO)
"""
# import nltk
# stopwords = nltk.download('stopwords')
from nltk.corpus import stopwords
# Do not change the sentences
sentence1 = "Socrates likes to watch movies. Mary likes movies too."
sentence2 = "Rene Descartes likes to watch movies. Mary likes movies too."
sentence3 = "Kant also likes to watch football games."


def collect_all_unique_words(list_of_sentences):
    res_list = []
    for i in list_of_sentences:
        a = i.split(" ")
        for j in a:
            if j not in res_list and j not in '':
                a = j.replace('.','')
                a = a.replace('\n', '')
                res_list.append(a)
    ad = []
    for v in res_list:
        if v not in ad:
            ad.append(v)
    return ad


def to_lowercase_and_remove_stop_words(list_of_sentences):
    res = list(map(lambda x: x.lower().replace('.',''), list_of_sentences))
    stop_words = stopwords.words('english')
    stop_iste = ['.', 'also', 'too']
    respons = list(filter(lambda x: x not in stop_words and x not in stop_iste, res))
    # resp = list(filter(lambda x: x not in stop_iste, respons))
    return respons


def create_matrix(dan, all_sentence):
    new_lests = []
    mat = []
    for i in dan:
        new_lests.append(list(map(str.lower,i)))
    for i in range(len(dan)):
        mat.append([])
    for i in all_sentence:
        for j in range(len(new_lests)):
            if i in new_lests[j]:
                mat[j].append(1)
            else:
                mat[j].append(0)
    mat.insert(0,dan)
    # s = zip(dan,mat)
    # print(list(mat))
    return mat
def output (Output):
    for i in Output:
        print(i)
def fun_work(Mas):
    list_un = collect_all_unique_words(Mas)
    lover = to_lowercase_and_remove_stop_words(list_un)
    mat = create_matrix(lover,Mas)
    output(mat)
    return  None

def matricks(file):
    result = file.split(".")
    return result

if __name__ == '__main__':

    # all_sentence = []
    # all_sentence.append(sentence1)
    # all_sentence.append(sentence2)
    # all_sentence.append(sentence3)
    all_sentence = matricks(open("test.txt").read())
    fun_work(all_sentence)

