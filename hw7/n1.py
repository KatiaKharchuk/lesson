a  = [[5,6,7,8,], [1,2,3,4], [5,6,7,8]]
b = [[1,2,3,4], [0,8,7,6], [5,6,7,8]]

from typing import Union, List

class Matrix:

    def __init__(self, lists: List[Union[list, str]]):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.list))

    def __add__(self, other):
        c = []
        for i in range(len(self.list)):
            c.append([])
            for j in range(len(self.list[0])):
                c[i].append(self.list[i][j] + other[i][j])
        return '\n'.join(map(str, c))

matrx1 = Matrix(a)
matrx2 = Matrix(b)

print(matrx1, '\n')
print(matrx2, '\n')
print(matrx1 + matrx2)