from collections import deque
from queue import PriorityQueue
import argparse
import copy

#takes maze txt files and converts them to arrays of strings (or 2D matrices, since we are programming in python)
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


#function to print the maze for visualization
def printMaze(mat):
    for i in mat:
        print(i)

#find our starting spot
def findStart(mat):
    row = 0
    for i in mat:
        col = 0
        row += 1
        for j in i:
            col += 1
            if (j == 'P'):
                return row - 1, col - 1
            else:
                continue
    print("P wasn't found if you can see this...feels bad man")

#function to find the goal point
def findEnd(mat):
    row = 0
    for i in mat:
        col = 0
        row += 1
        for j in i:
            col += 1
            if (j == '.'):
                return (row - 1, col - 1)
            else:
                continue
    print("P wasn't found if you can see this...feels bad man")

#function for safe transition for the frontier
def safeTransitions(mat, row, col, visited):
    return ((mat[row][col] != '%') and (
                (row, col) not in visited))


def findPathDFS(maze): 
    if maze == []:
        return maze
    strt = findStart(maze)
    final = DFS(strt[0], strt[1], maze)  # Go to DFS.
    return final

def findPathBFS(maze):
    if maze == []:
        return maze
    strt = findStart(maze)
    final = BFS(strt[0], strt[1], maze)  # Go to BFS.
    return final

def findPathGBFS(maze):
    if maze == []:
        return maze
    strt = findStart(maze)
    final = GreedyBest(strt[0], strt[1], maze)  # Go to Greedy Best.
    return final


def findPathAstar(maze):
    if maze == []:
        return maze
    strt = findStart(maze)
    final = Astar(strt[0], strt[1], maze)
    return final

def BFS(r, c, maze):
    q = deque()
    visited = set()
    q.append([(r, c)])
    while(len(q) != 0):
        
        #possible solution (list)
        current_list = q[0]

        # Last coordinate in the list is the current state... We want to know where to go from there.
        current_state = current_list[-1]

        # popleft from the queue
        q.popleft()

        # get coordinates
        row = current_state[0]
        col = current_state[1]

        #add current to visited set
        visited.add(current_state)
        
        # Found a possible goal state. Yes.
        if (maze[row][col] == "."):
            print("found baby", row, col)
            return current_list

        possible_actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for coord in possible_actions:
            dx = coord[0]
            dy = coord[1]

            if (safeTransitions(maze, row + dx, col + dy, visited)):
                temp_list = current_list.copy()
                temp_list.append((row + dx, col + dy))
                q.insert(0, temp_list)

def DFS(r, c, maze):
    visited = set()
    stack = []
    stack.append([(r, c)])

    while (len(stack) != 0):

        # Possible solution (a list)
        current_list = stack[-1]
        #print("current List:", current_list)

        # Last coordinate in the list is the current state... We want to know where to go from there.
        current_state = current_list[-1]

        # pop from the stack
        stack = stack[:len(stack) - 1]

        # Get coordinates
        row = current_state[0]
        col = current_state[1]

        # Add current state to the visited set
        visited.add(current_state)

        # yah = input("continue?") Credit to Ernest Quant for this debugging method

        # Found a possible goal state. Yes.
        if (maze[row][col] == "."):
            print("found baby", row, col)
            return current_list

        possible_actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for coord in possible_actions:
            dx = coord[0]
            dy = coord[1]

            if (safeTransitions(maze, row + dx, col + dy, visited)):
                temp_list = current_list.copy()
                temp_list.append((row + dx, col + dy))
                stack.insert(0, temp_list)


def ManhatDist(x1, y1, goal):
    return (abs(x1 - goal[0]) + abs(y1-goal[1]))
'''
def PqAdd(pq, r, c, goal):
    heuristic = (r, c, goal)
    for counter in range(len(pq)):
        if(heuristic < item[0]):
            pq.insert(counter, ())'''

def GreedyBest(r, c, maze):
    visited = set()
    goal = findEnd(maze)
    pq = [] #priority queue a list of solutions with the heuristics
    heuristic = ManhatDist(r, c, goal)
    pq.append(([(r,c)], heuristic))
    while(len(pq) != 0):
        #possible solution (list)
        current_list = pq[0][0]

        # Last coordinate in the list is the current state... We want to know where to go from there.
        current_state = current_list[-1]

        # popleft from the queue
        pq.pop(0)

        # get coordinates
        row = current_state[0]
        col = current_state[1]

        #add current to visited set
        visited.add(current_state)
        
        # Found a possible goal state. Yes.
        if (maze[row][col] == "."):
            print("found baby", row, col)
            return current_list

        possible_actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for coord in possible_actions:
            dx = coord[0]
            dy = coord[1]

            if (safeTransitions(maze, row + dx, col + dy, visited)):
                temp_list = current_list.copy()
                temp_list.append((row + dx, col + dy))
                temp_tup = (temp_list, ManhatDist(row+dx, col+dy, goal))
                pq.append(temp_tup)
                pq  = sorted(pq, key=lambda x: x[1])

def Astar(r, c, maze):
    visited = set()
    goal = findEnd(maze)
    pq = [] #priority queue a list of solutions with the heuristics
    heuristic = ManhatDist(r, c, goal)
    counter = 1
    func = counter + heuristic
    pq.append(([(r,c)], func))
    while(len(pq) != 0):
        #possible solution (list)
        current_list = pq[0][0]

        # Last coordinate in the list is the current state... We want to know where to go from there.
        current_state = current_list[-1]

        # popleft from the queue
        pq.pop(0)

        # get coordinates
        row = current_state[0]
        col = current_state[1]

        #add current to visited set
        visited.add(current_state)
        
        # Found a possible goal state. Yes.
        if (maze[row][col] == "."):
            print("found baby", row, col)
            return current_list

        possible_actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        counter += 1
        for coord in possible_actions:
            dx = coord[0]
            dy = coord[1]

            if (safeTransitions(maze, row + dx, col + dy, visited)):
                temp_list = current_list.copy()
                temp_list.append((row + dx, col + dy))
                heur = ManhatDist(row+dx, col+dy, goal)
                new_func = counter + heur
                temp_tup = (temp_list, new_func)
                pq.append(temp_tup)
                pq  = sorted(pq, key=lambda x: x[1])

def update_maze(maze, path):
    #convert every string in the list into another list
    stringLis = []

    for row in maze:
        stringLis.append(list(row))

    # mark the spots that are in the solution (path)
    for coord in path:
        stringLis[coord[0]][coord[1]] = "1"

    # maze with solution
    updated = []
    for i in stringLis:
        updated.append("".join(i))
    return updated


# you gotta print the maze a row at a time.
def print_maze(maze):
    for row in maze:
        print(row)


def main():
    argScan = argparse.ArgumentParser()
    argScan.add_argument("--method", required=True, help="mazeMethIn")
    argScan.add_argument("mazeNameIn")
    args = argScan.parse_args()
    mazeMethod = args.method
    print(mazeMethod)
    mazeName = args.mazeNameIn
    print(mazeName)

    maze2 = txtToMat(mazeName)

    if(mazeMethod == 'Greedy'):
        path2 = findPathGBFS(maze2)
        maze0 = update_maze(maze2, path2)
        print_maze(maze0)
    elif(mazeMethod == 'Depth'):
        path3 = findPathDFS(maze2)
        maze1 = update_maze(maze2, path3)
        print_maze(maze1)
    elif(mazeMethod == 'Breadth'):
        path4 = findPathBFS(maze2)
        maze2 = update_maze(maze2, path4)
        print_maze(maze2)
    elif(mazeMethod == 'Astar'):
        path5 = findPathAstar(maze2)
        maze3 = update_maze(maze2, path5)
        print_maze(maze3)


main()


'''Manhattan Distance Heuristic on a given node / space
    for rows
    	for cols \\preemptively assign each space its Manhattan distance value going linearly through the matrix. 
        if (node/space != %):
    		funct heuristic(node)
    			dx = absVal(node.x - goal.x)
      			dy = absVal(node.y - goal.y)

    For Best-First (Greedy) - Comparative
    	Just take the lowest out of a given set of heuristics from a node.
        Require us to implement a priority queue in order to keep track of costs of nodes.'''

"""To Do's using the nodes:
"""

