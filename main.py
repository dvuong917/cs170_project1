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
    def __lt__(self, other):
        return (self.cost < other.cost)
    
def expand(node, repeatSet): 
    print("parent:")
    printPuzzle(node.puzzle)
    children = []
    possibleMoves = [moveBlankLeft, moveBlankRight, moveBlankUp, moveBlankDown]
    for move in possibleMoves:
        newPuzzle = move(node.puzzle)
        if (newPuzzle):
            child = Node(node, newPuzzle, 0, node.depth+1)
            newTuple = child.puzzle_to_tuple()
            if (newTuple not in repeatSet):
                children.append(child)
                repeatSet.add(newTuple)
                print("child:")
                printPuzzle(newPuzzle)
            else:
                print("repeat child")

    # print("Children created: ")
    # for child in children:
    #     printPuzzle(child.puzzle)
    return children
    
def heuristic(depth, choice):
    if choice == 1: # uniform cost
        return depth
    elif choice == 2: # misplaced tile
        return depth + misplacedTile
    else: # manhattan distance
        return depth + manhattanDistance

def uniformCost(puzzle):
    starting_node = Node(None, puzzle, 0, 0)
    working_queue = []
    repeated_states = set()
    heapq.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    stack_to_print = [] # the board states are stored in a stack

    while len(working_queue) > 0:
        max_queue_size = max(len(working_queue), max_queue_size)
        # the node from the queue being considered/checked
        node_from_queue = heapq.heappop(working_queue)
        repeated_states.add(node_from_queue.puzzle_to_tuple())
        if node_from_queue.solved():
            print("SOLVED!")
            print("Number of nodes expanded:", num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            return node_from_queue
        else:
            for child in expand(node_from_queue, repeated_states):
                child.depth = node_from_queue.depth + 1
                child.cost = heuristic(node_from_queue.depth, 1)
                heapq.heappush(working_queue, child)

# Do not count the blank
def misplacedTile(puzzle):
    starting_node = Node(None, puzzle, 0, 0)

def manhattanDistance(puzzle):
    starting_node = Node(None, puzzle, 0, 0)

# Test Cases
depth0 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
depth2 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
depth4 = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
depth8 = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
depth12 = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]
depth16 = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]
depth20 = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
depth24 = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]
testDepth2Repeat = [[1, 2, 3], [0, 5, 6], [4, 7, 8]]
menuOn = True
while menuOn:
    choice = int(input("Select an algorithm. (1) Uniform Cost Search, (2) Misplaced Tile Heuristic, (3) Manhattan Distance Heuristic.\n"))
    if choice == 1:
        uniformCost(depth2)
        menuOn = False
    elif choice == 2:
        print("Choice 2")
        menuOn = False
    elif choice == 3:
        print("Choice 3")
        menuOn = False
    else:
        print("Invalid choice.")
        menuOn = True
