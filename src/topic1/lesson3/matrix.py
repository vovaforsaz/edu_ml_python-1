<<<<<<< HEAD
if __name__ == '__main__':

    M1 = [[1, 2, 3, 4, 11, 7, 8, 11],
=======
def main_matrix():
    M1 = [[1, 2, 3, 4, 11],
>>>>>>> 599e8f966929db85924e0497534e02ed0fff7780
          [5, -6, 7, 8, 11],
          [5, 2, -42, 8, 11,11, 100,11, 100,11, 100],
          [1, 6, 7, 11, 100]]

<<<<<<< HEAD
    print('Задание 1.вывести все данные с матрицы(со всех столбцов и строк матрица не квадратная', [M1])
    print('')
    for i in range(len(M1)):
        for j in range(len(M1[i])):
            print(M1[i][j])
    print('Completing the task №1')

    print('')
=======
    print('\n whole rectangular matrix')
    for i in range(len(M1[0]) - 1):
        print('\n')
        for j in range(len(M1[1])):
            print("|", M1[i][j], "|", end=" ")
>>>>>>> 599e8f966929db85924e0497534e02ed0fff7780


def main_diagonal():
    M2 = [[1, 2, 3, 4],
          [5, -6, 7, 8],
          [5, 6, 5, 8],
          [1, 6, 7, 11]]
<<<<<<< HEAD
    print('Задание 2 - есть квадратная матрица, необходимо вывести диагональ ( 1 значение 1-й строки, 2 значение 2-й и т.д.)', [M2])
    print('')
    a = []
    for i in range(len(M2)):
        for j in range(len(M2[i])):
            if i == j:
                a.append(M2[i][j])
    print(a)
    print('')
    print('Completing the task №2')

    print('')
=======
    print('\n Main diagonal of the matrix')
    for i in range(len(M2[0])):
        print(M2[i][i], end=" ")


def reverse_diagonal():
    print('\nReverse diagonal')
>>>>>>> 599e8f966929db85924e0497534e02ed0fff7780
    M3 = [[1, 2, 3, 4],
          [5, 2, 7, 8],
          [5, 6, 3, 8],
          [1, 6, 7, 4]]
<<<<<<< HEAD

    print('Задание 3 - вывести обратную диагональ квадратной матрицы( последнее значение последней строки, предпоследнее значение предпоследней строки, ...)', [M3])
    print('')
    b = []
    for i in reversed(range(len(M3))):
        for j in reversed(range(len(M3[i]))):
            if i == j:
                b.append(M3[i][j])
    print(b)
    print('')
    print('Completing the task №3 test')
=======
    matrix_size = len(M3[0])
    for i in range(matrix_size):
        print(M3[matrix_size - 1 - i][matrix_size - 1 - i], end=" ")


if __name__ == '__main__':
    main_matrix()
    main_diagonal()
    reverse_diagonal()
>>>>>>> 599e8f966929db85924e0497534e02ed0fff7780
