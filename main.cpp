#include <iostream>
#include <queue>

using namespace std;

#define N 3 // denotes size of matrix; change this to change the puzzle size

struct Node {
    int matrix[N][N];
    Node *next = nullptr;
    Node *prev = nullptr;
    // store coordinates of blank space
    int x, y; // x = row, y = col
};

queue<Node> nodesQueue;

int initialState[N][N] = {
    {1, 2, 3},
    {4, 0, 6},
    {7, 5, 8}
};

int goalState[N][N] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 0}
};

// define operators
void moveBlankLeft(int matrix[N][N], int x, int y) {
    if (y != 0) {
        matrix[x][y] = matrix[x][y-1];
    }
};
void moveBlankRight(int matrix[N][N], int x, int y) {
    if (y != N-1) {
        matrix[x][y] = matrix[x][y+1];
    }
};
void moveBlankUp(int matrix[N][N], int x, int y) {
    if (x != 0) {
        matrix[x][y] = matrix[x-1][y];
    }
};
void moveBlankDown(int matrix[N][N], int x, int y) {
    if (x != N-1) {
        matrix[x][y] = matrix[x+1][y];
    }
};

void printMatrix(int matrix[N][N]) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
};

int main() {
    printMatrix(initialState);
}
