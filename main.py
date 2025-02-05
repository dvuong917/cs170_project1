import heapq

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
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row][col-1]
        puzzle[row][col-1] = temp
        return puzzle
    else:
        return None
def moveBlankRight(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if col < n-1:
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row][col+1]
        puzzle[row][col+1] = temp
        return puzzle
    else:
        return None
def moveBlankUp(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if row > 0:
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row-1][col]
        puzzle[row-1][col] = temp
        return puzzle
    else:
        return None
def moveBlankDown(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if row < n-1:
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row+1][col]
        puzzle[row+1][col] = temp
        return puzzle
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
        print(puzzleTuple)
        return puzzleTuple
    
def expand(node, dict): 
    if (moveBlankLeft(node.puzzle) and moveBlankLeft(node.puzzle) not in dict):
        child1 = Node(node, moveBlankLeft(node.puzzle), 0, node.depth+1)
    if (moveBlankRight(node.puzzle) and moveBlankRight(node.puzzle) not in dict):
        child2 = Node(node, moveBlankRight(node.puzzle), 0, node.depth+1)
    if (moveBlankUp(node.puzzle) and moveBlankUp(node.puzzle) not in dict):
        child3 = Node(node, moveBlankUp(node.puzzle), 0, node.depth+1)
    if (moveBlankDown(node.puzzle) and moveBlankDown(node.puzzle) not in dict):
        child4 = Node(node, moveBlankDown(node.puzzle), 0, node.depth+1)

def uniformCost(puzzle):
    starting_node = Node(None, puzzle, 0, 0)
    working_queue = []
    repeated_states = dict()
    heapq.heappush(working_queue, starting_node)
    num_nodes_expanded = 0
    max_queue_size = 0
    repeated_states[starting_node.puzzle_to_tuple()] = "parent"
    print(list(repeated_states))

# Test Cases
depth0 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
depth2 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
depth4 = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
depth8 = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
depth12 = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]
depth16 = [[1, 6, 7], [5, 0, 3], [4, 8, 2]]
depth20 = [[7, 1, 2], [4, 8, 5], [6, 3, 0]]
depth24 = [[0, 7, 2], [4, 6, 1], [3, 5, 8]]

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
