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
from nltk.corpus import stopwords
# Do not change the sentences
sentence1 = "Socrates likes to watch movies. Mary likes movies too."
sentence2 = "Rene Descartes likes to watch movies. Mary likes movies too."
sentence3 = "Kant also likes to watch football games"


def collect_all_unique_words(list_of_sentences):
    res_list = []
    for i in list_of_sentences:
        a = i.split(" ")
        for j in a:
            if j not in res_list:
                res_list.append(j.replace('.',''))
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

def fun_work(Mas):
    list_un = collect_all_unique_words(Mas)
    lover = to_lowercase_and_remove_stop_words(list_un)
    create_matrix(lover,Mas)
    return  None


if __name__ == '__main__':
    '''
    we need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''
    all_sentence = []
    all_sentence.append(sentence1)
    all_sentence.append(sentence2)
    all_sentence.append(sentence3)
    fun_work(all_sentence)
    # print()

    # TODO 3 create the matrix where count of COLUMNS is unique words and ROWS count of sentences

    # https://www.baeldung.com/cs/convert-word-to-vector#one-hot-vectors
    # vector where each column corresponds to a word
