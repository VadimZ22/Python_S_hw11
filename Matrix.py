# Создайте класс Матрица.
# Добавьте методы для:
# ○вывода на печать,
# ○сравнения,
# ○сложения,
# ○*умножения матриц

class Matrix:


    def __init__(self, matrix: list = []):
        if isinstance(matrix, list) and isinstance(matrix[0], list):
            for i in range (1, len(matrix)):
                if len(matrix[i]) != len(matrix[0]):
                    raise ValueError('Это не матрица!')
            self.matrix = matrix
        else:
            raise ValueError('Это не матрица!')

    def __add__(self, other):
        result =[]
        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix):
                for i in range(0, len(self.matrix)):
                    if len(self.matrix[i]) != len(other.matrix[i]):
                        raise ValueError('Матрицы разные, операция невозможна!')
                    res2 = []
                    for j in range(0, len(self.matrix[i])):
                        res = self.matrix[i][j] + other.matrix[i][j]
                        res2.append(res)
                    result.append(res2)
                return Matrix(result)
            return NotImplemented('Матрицы разные, операция невозможна!')
        return NotImplemented('Второй элемент не принадлежит классу Matrix')



    def __eq__(self, other):
        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix):
                for i in range(0, len(self.matrix)):
                    if len(self.matrix[i]) != len(other.matrix[i]):
                        raise ValueError('Матрицы разные, операция невозможна!')
                    for j in range(0, len(self.matrix[i])):
                        if self.matrix[i][j] != other.matrix[i][j]:
                            return False
                return True
            return NotImplemented('Матрицы разные, операция невозможна!')
        return NotImplemented('Второй элемент не принадлежит классу Matrix')


    def __str__(self):
        return f'{self.matrix}'



arr1 = [[1,2,3], [4,5,6], [7,8,9]]
arr2 = [[3,2,1], [6,5,4], [9,8,7]]
arr3 = [[3,2,1], [6,5,4], [9,8,7]]
m = Matrix(arr1)
p = Matrix(arr2)
z = Matrix(arr3)
print(m)
print(m + p)
print(z == p)
# _________________ВЫВОД_________________
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[4, 4, 4], [10, 10, 10], [16, 16, 16]]
# True
