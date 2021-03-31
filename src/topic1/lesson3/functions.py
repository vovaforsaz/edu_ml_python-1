"""
 Functions are a convenient way to divide your code into useful blocks,
 allowing us to order our code, make it more readable, reuse it and save some time.
 Also functions are a key way to define interfaces so programmers can share their code.
"""
from functools import reduce


def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    '''
    Functions may return a value to the caller, using the keyword- 'return' . For example:
    '''
    listens = []
    listens.append(a)
    listens.append(b)

    return listens

def sum_two_numbers_2(a, b):
    '''
    Functions may return a value to the caller, using the keyword- 'return' . For example:
    '''
    return a + b
# функция поиск по определённой букве в слове вычитка из массива
def search_for_a_specific_letter(search, param,including=None):
    if(including == False):
        return list(filter(lambda x: search not in x, param))
    else:
        return list(filter(lambda x: search in x, param))


lambda_multiply_2 = lambda x: x * 2
lambda_sqrt_2 = lambda x: x ** 2

if __name__ == '__main__':
    my_function()
    my_function_with_args("Student", "good luck")
    # print(sum_two_numbers(1,2))
    M2 = ['sa','scd','scdc','sdcs']
    res = map(str.upper, M2)
    print(list(res))
    ast = lambda x: x * 3
    lisy_nimbrt = [1,2,3,4,5]
    lisy_nimbrtssss = ['sa','scd','scdc','sdcs']
    res = map(lambda x: x ** 3, lisy_nimbrt)
    print(list(res))

    print('-zip--')
    res = list(zip(lisy_nimbrtssss,lisy_nimbrt))
    print(res)
    print(lambda_multiply_2(5))
    print(lambda_sqrt_2(5))

    my_pets = ['alfred', 'tabitha', 'william', 'arla', "test"]
    for i in my_pets:
        print(i.upper())

    # HOF High order function
    # map
    # map(func, *iterables) --> map object
    res = list(map(str.upper, my_pets))
    print(res)

    # 2
    list_number = [1, 2, 3, 4]
    res = map(lambda x: x ** 2, list_number)
    print(list(res))

    # 3
    list_number = [1, 2, 3, 4]
    list_words = ["one", "qwer", "ett", "rttr"]
    res_zip = list(zip(list_number, list_words))
    print(res_zip)

    # TODO
    print("--------------start home_test filter----------------------")
    home_filter = ['alfred',
                   'tabitha',
                   'william',
                   'arla',
                   "test",
                   'likes',
                   'vova',
                   'work',
                   'home',
                   'movies',
                   'Socrates']
    print(search_for_a_specific_letter('a',home_filter,False))
    print("--------------final home_test filter----------------------")
    # filter()
    # reduce()


def function_task1():
    """
    Modify this function to return a list of strings
    """
    lis = sum_two_numbers("1","2")
    return lis


def function_task2(list1, list2):
    """
    Modify this function to return concatenated lists
    """
    lis = sum_two_numbers_2(list1, list2)
    return lis
