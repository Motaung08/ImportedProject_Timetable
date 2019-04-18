class GraphColoring():
    def __init__(self, vertexCount, theParameter):

        self.adjacencyMatrix = []
        self.vertexCount = vertexCount
        self.vertexColours = []
        self.clashes = []
        self.clashParameter = theParameter
        self.maxSessions = 6

        for i in range(0, self.vertexCount):
            temp = [0] * vertexCount
            self.adjacencyMatrix.append(temp)

        # print(self.adjacencyMatrix)
        self.vertexColours = [[]] * vertexCount
        print(self.vertexColours)

    def getWeight(self, course1, course2):
        weight = 0
        if len(course1) >= len(course2):
            for i in range(0, len(course2)):
                if course2[i] in course1:
                    weight = weight + 1
        else:
            for i in range(0, len(course1)):
                if course1[i] in course2:
                    weight = weight + 1

        return weight

    def addEdge(self, i, j, weight):
        if (i >= 0 and i < self.vertexCount) and (j >= 0 and j < self.vertexCount) and (i != j):
            self.adjacencyMatrix[i][j] = weight
            self.adjacencyMatrix[j][i] = weight

    def isEdge(self, i, j):
        if (i >= 0 and i < self.vertexCount) and (j >= 0 and j < self.vertexCount):
            if (adjacencyMatrix[i][j] != 0):
                return true
            else:
                return false

    def getNeighbours(self, vertex):
        neighbours = []

        for i in range(0, len(self.adjacencyMatrix)):
            if self.adjacencyMatrix[i][vertex] != 0:
                neighbours.append(i)

        return neighbours

    def getDegree(self, vertex):
        degree = len(self.getNeighbours(vertex))

        return degree

    def setColour(self, vertex, finalCourses):
        colour = -1
        usedColours = []
        neighbours = self.getNeighbours(vertex)

        for i in range(0, len(neighbours)):
            if len(self.vertexColours[neighbours[i]]) != 0:
                for j in range(0, len(self.vertexColours[neighbours[i]])):
                    usedColours.append(self.vertexColours[neighbours[i]][j])

        for c in range(0, len(usedColours) + 1):

            if c not in usedColours and c not in self.vertexColours[vertex]:
                self.vertexColours[vertex].append(c)

            if (len(self.vertexColours[vertex]) == len(finalCourses[vertex])):
                break











