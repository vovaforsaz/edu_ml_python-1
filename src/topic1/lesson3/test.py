
my_pets = ['alfred', 'tabitha', 'william', 'arla', "test",'likes','movies','Socrates']
sentence1 = "Socrates likes to watch movies. Mary likes movies too."
sentence2 = "Rene Descartes likes to watch movies. Mary likes movies too."
sentence3 = "Kant also likes to watch football games"
arr = (filter(lambda x: 'a' in x, my_pets))
print(list(arr))
print(*filter(lambda x: 'e' in x, my_pets))
print('-------------')
res = list(filter(lambda x: 'a' not in x, my_pets))
print(res)
print('-------------')
# функция поиск по определённой букве в слове вычитка из массива
def search_for_a_specific_letter(search, param):
    return list(filter(lambda x: search in x, param))

test = search_for_a_specific_letter('a',my_pets)
print(test)