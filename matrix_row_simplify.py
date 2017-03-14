#化简矩阵为行最简矩阵，已测试多种特殊情况，暂未发现bug
#由吉林大学开放源技术协会编写于 2017年3月13日

import os

class matrix_row_simplify():
    def __init__(self):
        self.matrix = list()
        self.row = 0
        self.divide_zero = 0
        self.input_matrix()
        self.is_matrix()
        for i in range(0,self.column):
            if i < self.row:
                self.column_simplify(i)
            else:
                break
        print("\nThe result is:")
        for i in range(0,self.row):
            for j in range(0,self.column):
                self.matrix[i][j] = round(self.matrix[i][j],2)
        for i in self.matrix:
            print(i)

        self.q = input("\nThank you for using!\nPress ENTER to quit...")


    def input_matrix(self):
        print("The program to simplify the matrix on row.")

        print("Now, let us to input matrix which you want to simplify.")
        print("You can break input by insert any word(No number).\n")
        while True:
            self.matrix.append(input("Please input the " + format(self.row + 1,"d") +" row(Element divided by SPACE):"))
            if self.matrix[self.row].isalpha():
                self.matrix.pop()
                break
            self.matrix[self.row] = self.matrix[self.row].split()
            self.row += 1
        for i in range(0,len(self.matrix)):
            for j in range(0,len(self.matrix[i])):
                self.matrix[i][j]=eval(self.matrix[i][j])
        #self.row -= 1

    def is_matrix(self):
        for i in self.matrix:
            if len(i) != len(self.matrix[0]):
                print("Error:You have not insert a matrix! You see see what you did!\n")
                for i in self.matrix:
                    print(i)
                os._exit(0)
        self.column = len(self.matrix[0])

    def column_simplify(self, c):
        self.sum_row_and_divide(c)
        if self.divide_zero == 0:
            self.remove_column_element(c)



    def sum_row_and_divide(self, r):
        for i in range(r,self.column):
            for j in range(r,self.row):
                if j == r:
                    continue
                else:
                    self.matrix[r][i] += self.matrix[j][i]
        self.divide = self.matrix[r][r]
        if self.divide != 0:
            for k in range(r,self.column):
                self.matrix[r][k] /= self.divide
        else:
            self.divide_zero = 1

    def remove_column_element(self,c):
        for i in range(0,self.row):
            self.temp = self.matrix[i][c]
            if i == c:
                continue
            else:
                for j in range(c,self.column):
                    self.matrix[i][j] -= self.temp * self.matrix[c][j]

matrix_row_simplify()