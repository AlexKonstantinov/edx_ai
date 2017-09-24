import sys
import copy

class Solution:

    def __init__(self, data):
        self.__initialState = copy.copy(data)
        self.__goal = [0,1,2,3,4,5,6,7,8]
        self.__actions = ['up', 'down', 'left', 'right']
        print(data[4])
    def bfs(self):
        equality = True
        for index, elem in enumerate(self.__goal):
            if self.__initialState[index] != elem:
                equality = False
        if equality:
            print('ok')
        else:
            print('not ok')
    def dfs(self):
        a = 0
    def ast(self):
        b = 0
test = Solution(sys.argv[1].split(','))
test.bfs()

