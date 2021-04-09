import unittest
from src.topic2.word_to_vector import collect_all_unique_words, to_lowercase_and_remove_stop_words


class MyTestCase(unittest.TestCase):

    def test_collect_all_unique_words(self):
        self.assertEqual(collect_all_unique_words(['a', 'b', 'c', 'a', 'a', 'c']), ['a', 'b', 'c'])

    def test_to_lowercase_and_remove_stop_words(self):
        self.assertEqual(to_lowercase_and_remove_stop_words(['Hello', 'ABC', 'to', 'and']), ['hello', 'abc'])

    def test_lowercase_and_remove_stop_words(self):
        stop_words_list = ["to", "and"]
        self.assertEqual(to_lowercase_and_remove_stop_words(['Hello', 'ABC', 'to', 'and'], stop_words_list),
                         ['hello', 'abc'])


if __name__ == '__main__':
    unittest.main()
