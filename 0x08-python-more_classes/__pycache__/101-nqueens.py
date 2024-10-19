import sys

def print_solutions(solutions):
    """Print all the solutions in the required format."""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the same column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    """Use backtracking to find all solutions."""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)

def nqueens(n):
    """Initialize the board and solve the N-Queens problem."""
    board = [-1] * n  # Initialize the board
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    nqueens(N)
import sys

def print_solutions(solutions):
    """Print all the solutions in the required format."""
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check the same column
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    """Use backtracking to find all solutions."""
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)

def nqueens(n):
    """Initialize the board and solve the N-Queens problem."""
    board = [-1] * n  # Initialize the board
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is an integer
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    nqueens(N)
