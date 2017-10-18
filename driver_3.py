import sys
import copy

class Element:
    def __init__(self, element, shift):
        self.element = []
        self.parent = []
        self.__shift = {
            1: -3,
            2: 3,
            3: -1,
            4: 1
        }
        if shift == 0:
            for index, elem in enumerate(element):
                self.element.append(int(elem))
            self.parent = None
            self.backDirection = None
        else:
            self.element = copy.copy(element.element)
            for index, elem in enumerate(self.element):
                self.parent.append(int(elem))
            self.swap(shift)
            self.backDirection = shift
    def getZeroPosition(self):
        return self.element.index(0)
    def swap(self, action):
        zeroIndex = self.getZeroPosition()
        shiftPosition = self.__shift[action]
        self.element[zeroIndex + shiftPosition] = self.element[zeroIndex + shiftPosition] + self.element[zeroIndex]
        self.element[zeroIndex] = self.element[zeroIndex + shiftPosition] - self.element[zeroIndex]
        self.element[zeroIndex + shiftPosition] = self.element[zeroIndex + shiftPosition] - self.element[zeroIndex]

class Solution:

    def __init__(self, data):
        self.currentState = None
        self.__pathToGoal = []
        self.__nodesExpanded = 0
        self.explored = [Element(data, 0)]
        self.visited = []
        self.__goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.__actions = {
            1: 'Up',
            2: 'Down',
            3: 'Left',
            4: 'Right'
        }
        self.__availableDirections = {
            0: [2, 4],
            1: [2, 3, 4],
            2: [2, 3],
            3: [1, 2, 4],
            4: [1, 2, 3, 4],
            5: [1, 2, 3],
            6: [1, 4],
            7: [1, 3, 4],
            8: [1, 3]
        }
    def getPathToGoal(self):
        curElem = self.visited[len(self.visited)-1]
        while not(curElem.backDirection is None):
            self.__pathToGoal.append(self.__actions[curElem.backDirection])
            for index, elem in enumerate(self.visited):
                if not(elem.element is None):
                    if (self.__arrayEqual(curElem.parent, elem.element)):

                        curElem = elem
                        break
        return list(reversed(self.__pathToGoal))
    def getCostOfPath(self):
        return len(list(reversed(self.__pathToGoal)))
    def getNodesExpanded(self):
        return self.__nodesExpanded
    def bfs(self):
        self.currentState = self.explored.pop(0)
        self.visited.append(self.currentState)
        self.__explore(self.currentState)
        while not(self.__checkGoal(self.currentState.element)):
            self.currentState = self.explored.pop(0)
            self.visited.append(self.currentState)
            if (self.__explore(self.currentState) > 0):
                self.__nodesExpanded = self.__nodesExpanded + 1
    def dfs(self):
        a = 0
    def aStar(self):
        b = 0
    def __checkGoal(self, currentState):
        equality = True
        for index, elem in enumerate(self.__goal):
            if currentState[index] != elem:
                equality = False
        return equality
    def __explore(self, current):
        zeroIndex = current.getZeroPosition()
        avDirsForCurrent = self.__availableDirections[zeroIndex]
        counter = 0
        for index, elem in enumerate(avDirsForCurrent):
            tmpElem = Element(current, elem)
            if not (self.isVisited(tmpElem)):
                self.explored.append(tmpElem)
                counter = counter + 1
            else:
                del tmpElem
        return counter

    def isVisited(self, el):
        res = False
        for index, elem in enumerate(self.explored):
            if self.__arrayEqual(elem.element, el.element):
                res = True
                return res
        for index2, elem2 in enumerate(self.visited):
            if self.__arrayEqual(elem2.element, el.element):
                res = True
                return res
        return res
    def __arrayEqual(self, arr1, arr2):
        res = True
        if len(arr1) == len(arr2):
            for index, elem in enumerate(arr1):
                if elem != arr2[index]:
                    res = False
                    return res
        else:
            res = False
            return res
        return res
test = Solution(sys.argv[1].split(','))
test.bfs()
print(test.getPathToGoal())
print(test.getCostOfPath())
print(test.getNodesExpanded())

