"""
 Functions are a convenient way to divide your code into useful blocks,
 allowing us to order our code, make it more readable, reuse it and save some time.
 Also functions are a key way to define interfaces so programmers can share their code.
"""


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


    res = list(zip(lisy_nimbrtssss,lisy_nimbrt))
    print(res)
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
