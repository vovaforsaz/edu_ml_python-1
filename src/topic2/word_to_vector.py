"""
Why word vectors?

Word Embedding is a language modeling technique used for mapping words to vectors of real numbers.
It represents words or phrases in vector space with several dimensions.

Poetry is, at its core, the art of identifying and manipulating linguistic similarity.
similarity and simple linear algebra

@see https://www.baeldung.com/cs/convert-word-to-vector

"""


def collect_all_unique_words(list_of_words):
    """
    1. all unique words have to be collected to the list
    """
    # example 1
    # unique_words = list(set(list_of_sentences))

    # example 2
    unique_words = list()
    for w in list_of_words:
        if unique_words.count(w) == 0:
            unique_words.append(w)

    unique_words.sort(reverse=False)
    return unique_words


def to_lowercase_and_remove_stop_words(list_of_words, stop_words_list):
    """
    1. Uppercase should be transform to lower case. For example 'Hello' -> 'hello'
    2. Remove all STOP WORDS like - 'too, and, etc'

    """
    res = list(filter(lambda x: stop_words_list.count(x) == 0, list_of_words))
    res = list(map(lambda x: x.lower(), res))
    return res


class matrixObject():

    def __init__(self, count_of_columns, stop_words_list=None, matrix_title_list=None):
        if stop_words_list is None: stop_words_list = []
        if matrix_title_list is None: matrix_title_list = []
        self.count_of_columns = count_of_columns
        self.stop_words_list = stop_words_list
        self.matrix_title_list = matrix_title_list
        self.vector_matrix = []

    def update_title(self, list_of_words):
        res = collect_all_unique_words(list_of_words)
        res = to_lowercase_and_remove_stop_words(res, self.stop_words_list)
        return res

    def extend_matrix(self, list_of_words):
        res = self.update_title(list_of_words)
        self.matrix_title_list = collect_all_unique_words(res + self.matrix_title_list)
        self.vector_matrix.append(list(map(lambda w: res.count(w), self.matrix_title_list)))

    def print_matrix(self):
        print(self.matrix_title_list)
        list(map(lambda w: print(w), self.vector_matrix))


if __name__ == '__main__':

    list_for_matrix = ["Socrates Socrates likes to watch movies. Mary likes movies too.",
                       "Rene Descartes likes to watch movies. Mary likes movies too.",
                       "Kant, also likes to watch football games",
                       "Test",
                       "Hello"]

    '''
    We need to deal with linguistic entities such as words?
    How can we model them as mathematical representations? The answer is we convert them to vectors!
    '''
    matrix = matrixObject(count_of_columns=10)
    for i in list_for_matrix:
        matrix.extend_matrix(i.split())

    matrix.print_matrix()