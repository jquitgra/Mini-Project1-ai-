#you need argument parser (import argparse)
class Node:
    def __init__(self, data, child):
        self.data = data
        self.child = child
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def getChild(self):
        return self.child
        
def txtToMat(fname):
    retM = []
    with open(fname) as myfile:
        for line in myfile:
            lineStr = ""
            line = line.strip()
            for tok in line:
                lineStr += tok
            retM.append(lineStr)
        return retM

def printMaze(mat):
    for i in mat:
        print(i)

'''def safeTransitions(mat, row, col, visited):
    print(row, col, "\n")
    return ((mat[row][col] != "%") and ((row, col) not in visited) and (row >= 0) and (col >= 0))'''

def findStart(mat):
    row = 0
    for i in mat:
        col = 0
        row +=1
        for j in i:
            col += 1
            if(j == 'P'):
                return row-1, col-1
            else:
                continue
    print("P wasn't found if you can see this...feels bad man")

def safeTransitions(mat, row, col, visited):
    return ((mat[row][col] != '%')and((row, col) not in visited))

def findPath(maze):  
    maze = txtToMat('Maze1.txt')
    if maze == []:
        return maze
    strt = findStart(maze)
    final = DFS(strt[0], strt[1], maze)
    return final

def DFS(r, c, maze):
    visited = set()
    stack = []
    stack.append((r,c))
    
    while(len(stack) != 0):
        row = stack[-1][0]
        col = stack[-1][1]
        visited.add((row, col))
        stack.pop()
        if (safeTransitions(maze, row, col, visited)):
            print(row,col, "\n")
            maze[row][col].replace(" ", "1")
            visited.add((row, col))

        elif(maze[row][col]== "."):
            print("found baby", row, col)
            return visited
        for i in range(-1, 2):
            for j in range(-1,2):
                if(safeTransitions(maze, row+i, col+j, visited)):
                    stack.append((row+i, col+j))
                    visited.add((row+i, col+j))

def printPath(M, visited):
    for i, j in visited:
        M[i][j].replace(" ", "1")
    return M

def main():
    maze = txtToMat("Maze1.txt")
    findPath(maze)
    print(visited)
    print(printPath(maze, visited))


main()
