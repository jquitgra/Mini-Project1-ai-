#you need argument parser (import argparse)
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

def safeTransitions(mat, row, col, visited):
    return ((mat[row][col] != '%')and((row, col) not in visited))

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

def findEnd(mat):
    row = 0
    for i in mat:
        col = 0
        row += 1
        for j in i:
            col += 1
            if(j == '.'):
                print(j, row-1, col-1)
                return
            else:
                continue
    print(". wasn't found if you can see this...feels bad man")


def findPath():
    visited = set()
    maze = txtToMat('Maze1.txt')
    final = []
    def DFS(r, c):
        visited.add((r,c))

        if(maze[r][c] == "."):
            return maze
            
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(safeTransitions(maze, r+i, c+j, visited)):
                    maze[r+i][c+j].replace(" ", "1")
                    DFS(r+i, c+j)
                        
    strt = findStart(maze)
    final = DFS(strt[0], strt[1])
    return final

def main():
    print(findPath())

main()

'''for string in mat:
        for letter in string:

    def DFS(r, c):
        if()
'''
