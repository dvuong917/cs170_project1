import heapq
import copy

n = 3

def findBlank(puzzle):
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == 0:
                return (i, j)
    return None

# Define operators
def moveBlankLeft(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if col > 0:
        newPuzzle = copy.deepcopy(puzzle)
        temp = newPuzzle[row][col]
        newPuzzle[row][col] = newPuzzle[row][col-1]
        newPuzzle[row][col-1] = temp
        return newPuzzle
    else:
        return None
def moveBlankRight(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if col < n-1:
        newPuzzle = copy.deepcopy(puzzle)
        temp = newPuzzle[row][col]
        newPuzzle[row][col] = newPuzzle[row][col+1]
        newPuzzle[row][col+1] = temp
        return newPuzzle
    else:
        return None
def moveBlankUp(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if row > 0:
        newPuzzle = copy.deepcopy(puzzle)
        temp = newPuzzle[row][col]
        newPuzzle[row][col] = newPuzzle[row-1][col]
        newPuzzle[row-1][col] = temp
        return newPuzzle
    else:
        return None
def moveBlankDown(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if row < n-1:
        newPuzzle = copy.deepcopy(puzzle)
        temp = newPuzzle[row][col]
        newPuzzle[row][col] = newPuzzle[row+1][col]
        newPuzzle[row+1][col] = temp
        return newPuzzle
    else:
        return None

def printPuzzle(puzzle):
    for i in range(n):
        print(f"{puzzle[i]}")
    print()

class Node:
    def __init__(self, parent, puzzle, cost, depth):
        self.parent = parent
        self.puzzle = puzzle
        self.cost = cost
        self.depth = depth
    def solved(self):
        if (self.puzzle == depth0):
            return True
        return False
    def puzzle_to_tuple(self):
        puzzleTuple = tuple(tuple(row) for row in self.puzzle)
        return puzzleTuple
    # Needed because heapq needs to compare nodes and pick the lower cost one
    def __lt__(self, other):
        return (self.cost < other.cost)
    
def expand(node, repeatedStates): 
    #print("parent:")
    #printPuzzle(node.puzzle)
    children = []
    possibleMoves = [moveBlankLeft, moveBlankRight, moveBlankUp, moveBlankDown]
    for move in possibleMoves:
        newPuzzle = move(node.puzzle)
        if (newPuzzle):
            child = Node(node, newPuzzle, 0, node.depth+1)
            newTuple = child.puzzle_to_tuple()
            if (newTuple not in repeatedStates):
                children.append(child)
                repeatedStates[child.puzzle_to_tuple()] = child.depth
                #print("child:")
                #printPuzzle(newPuzzle)
            # If child is repeated state, check if its dept is lower than the repeated state in dict
            # If so, replace repeatedStates with better depth and add child
            elif ((newTuple in repeatedStates) and (child.depth < repeatedStates.get(newTuple))):
                repeatedStates[newTuple] = child.depth
                children.append(child)
            # else:
            #     print("Repeat child")
                

    # print("Children created: ")
    # for child in children:
    #     printPuzzle(child.puzzle)
    return children
    
def heuristic(node, choice):
    if choice == 1: # uniform cost
        return node.depth
    elif choice == 2: # misplaced tile
        return numMisplaced(node.puzzle)
    else: # manhattan distance
        return distance(node.puzzle)

def search(puzzle, option):
    starting_node = Node(None, puzzle, 0, 0)
    working_queue = []
    repeated_states = dict()
    heapq.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    solutionPath = []
    solutionDepth = 0
    repeated_states[starting_node.puzzle_to_tuple()] = starting_node.depth

    print("\n========== TRACEBACK ==========")
    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        # the node from the queue being considered/checked
        node_from_queue = heapq.heappop(working_queue)
        if (option == 1):
            print("The best state to expand with g(n) = ", node_from_queue.depth, " and h(n) = 0 is...")
        elif (option == 2 or option == 3):
            print("The best state to expand with g(n) = ", node_from_queue.depth, " and h(n) = ", heuristic(node_from_queue, option), " is...")
        printPuzzle(node_from_queue.puzzle)
        repeated_states[node_from_queue.puzzle_to_tuple()] = node_from_queue.depth #store puzzle tuple + depth
        if node_from_queue.solved():
            print("\n========== Solution Path ==========")
            solutionDepth = node_from_queue.depth
            curr = node_from_queue
            while(curr != None):
                solutionPath.append(curr.puzzle)
                curr = curr.parent
            solutionPath.reverse()
            for nodePuzzle in solutionPath:
                printPuzzle(nodePuzzle)
            print("Solution depth:", solutionDepth)
            print("Number of nodes expanded:", num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            return node_from_queue
        else:
            for child in expand(node_from_queue, repeated_states):
                child.cost = child.depth + heuristic(child, option)
                heapq.heappush(working_queue, child)
            num_nodes_expanded += 1


# Do not count the blank
def numMisplaced(puzzle):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    numTiles = 0
    for i in range(0, n):
        for j in range(0, n):
            #print("Checking", goal[i][j], "with", puzzle[i][j])
            if (puzzle[i][j] != 0 and goal[i][j] != puzzle[i][j]): # Ignore blank tile and check if tile is in correct location
                numTiles += 1
    #print("Number of misplaced tiles: ", numTiles)
    return numTiles

def findNum(puzzle, num):
    for i in range(n):
        for j in range(n):
            if puzzle[i][j] == num:
                return (i, j)
    return None

def distance(puzzle):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0
    for i in range(0, n):
        for j in range(0, n):
            if (puzzle[i][j] != 0 and goal[i][j] != puzzle[i][j]): # Ignore blank tile and check if tile is in correct location
                puzzleRow, puzzleCol = findNum(puzzle, puzzle[i][j])
                goalRow, goalCol = findNum(goal, puzzle[i][j])
                #print("puzzle coords: ", puzzleRow, puzzleCol)
                #print("goal coords: ", goalRow, goalCol)
                distance += (abs(goalRow-puzzleRow) + abs(goalCol-puzzleCol))
    #print("Distance: ", distance)
    return distance

# Test Cases
depth0 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
depth2 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
depth4 = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
depth8 = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
depth12 = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]
depth16 = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]
depth20 = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
depth24 = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]
test = [[1, 2, 4], [3, 0, 6], [7, 8, 5]]

def selectPuzzleMenu():
    menuOn = True
    while menuOn:
        choice = int(input("Type '1' to use a default puzzle, or '2' to create your own.\n"))
        if choice == 1:
            return defaultPuzzleMenu()
        elif choice == 2:
            return createPuzzle()
        else:
            print("Invalid choice.")
            menuOn = True

def createPuzzle():
    print("Enter your puzzle, using a zero to represent the blank. " + 
        "Please only enter valid 8-puzzles. Separate the numbers with a space. " + 
        "RET only when finished." + '\n')
    puzzle_row_one = input("Enter the first row: ")
    puzzle_row_two = input("Enter the second row: ")
    puzzle_row_three = input("Enter the third row: ")
    puzzle_row_one = puzzle_row_one.split()
    puzzle_row_two = puzzle_row_two.split()
    puzzle_row_three = puzzle_row_three.split()
    for i in range(0, 3):
        puzzle_row_one[i] = int(puzzle_row_one[i])
        puzzle_row_two[i] = int(puzzle_row_two[i])
        puzzle_row_three[i] = int(puzzle_row_three[i])
    userPuzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
    print()
    return userPuzzle

def defaultPuzzleMenu():
    menuOn = True
    while menuOn:
        choice = int(input("Select a puzzle: (1) Depth 2, (2) Depth 4, (3) Depth 8, (4) Depth 12, (5) Depth 16, (6) Depth 20, (7) Depth 24.\n"))
        if choice == 1:
            return depth2
        elif choice == 2:
            return depth4
        elif choice == 3:
            return depth8
        elif choice == 4:
            return depth12
        elif choice == 5:
            return depth16
        elif choice == 6:
            return depth20
        elif choice == 7:
            return depth24
        else:
            print("Invalid choice.")
            menuOn = True            

def searchMenu(puzzle):
    menuOn = True
    while menuOn:
        choice = int(input("Select an algorithm. (1) Uniform Cost Search, (2) Misplaced Tile Heuristic, (3) Manhattan Distance Heuristic.\n"))
        if choice == 1:
            search(puzzle, 1)
            menuOn = False
        elif choice == 2:
            search(puzzle, 2)
            menuOn = False
        elif choice == 3:
            search(puzzle, 3)
            menuOn = False
        else:
            print("Invalid choice.")
            menuOn = True

puzzle = selectPuzzleMenu()
searchMenu(puzzle)