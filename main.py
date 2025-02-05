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
def moveBlankRight(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if col < n-1:
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row][col+1]
        puzzle[row][col+1] = temp
def moveBlankUp(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if row > 0:
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row-1][col]
        puzzle[row-1][col] = temp
def moveBlankDown(puzzle):
    blank = findBlank(puzzle)
    row, col = blank
    if row < n-1:
        temp = puzzle[row][col]
        puzzle[row][col] = puzzle[row+1][col]
        puzzle[row+1][col] = temp

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

def uniformCost(puzzle):
    starting_node = Node.Node(None, puzzle, 0, 0)
    working_queue = []

# Test Cases
depth0 = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
depth2 = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]
depth4 = [[1, 2, 3], [5, 0, 6], [4, 7, 8]]
depth8 = [[1, 3, 6], [5, 0, 2], [4, 7, 8]]
depth12 = [[1, 3, 6], [5, 0, 7], [4, 8, 2]]

moveBlankLeft(depth0)
printPuzzle(depth0)
moveBlankUp(depth0)
printPuzzle(depth0)
moveBlankRight(depth0)
printPuzzle(depth0)
moveBlankDown(depth0)
printPuzzle(depth0)

menuOn = True
while menuOn:
    choice = int(input("Select an algorithm. (1) Uniform Cost Search, (2) Misplaced Tile Heuristic, (3) Manhattan Distance Heuristic.\n"))
    if choice == 1:
        print("Choice 1")
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
