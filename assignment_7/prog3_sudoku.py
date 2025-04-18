"""
    CS472 - Assignment 7, program 3, Computational Complexity
    Shakufa Shendrik
    Sudoku solver
"""

import networkx as nx
from networkx.algorithms.coloring import greedy_color

# Function to convert a Sudoku grid into a graph
def sudoku_to_graph(sudoku):
    G = nx.Graph()
    # Create nodes for each cell in the 9x9 grid
    for row in range(9):
        for col in range(9):
            G.add_node((row, col), value=sudoku[row][col])

    # Add edges between nodes that are in the same row, column, or block
    for row in range(9):
        for col in range(9):
            for r2 in range(row + 1, 9):
                G.add_edge((row, col), (r2, col))  # Same column
            for c2 in range(col + 1, 9):
                G.add_edge((row, col), (row, c2))  # Same row
            # Add edges for the 3x3 subgrid
            block_row_start = (row // 3) * 3
            block_col_start = (col // 3) * 3
            for r in range(block_row_start, block_row_start + 3):
                for c in range(block_col_start, block_col_start + 3):
                    if (r, c) != (row, col):
                        G.add_edge((row, col), (r, c))  # Same block

    return G

# Function to solve the Sudoku using the graph coloring
def solve_sudoku(sudoku):
    G = sudoku_to_graph(sudoku)
    
    # Use greedy coloring to assign numbers (1-9) to nodes (cells in Sudoku)
    coloring = greedy_color(G, strategy="largest_first")
    
    # Reconstruct the Sudoku grid from the coloring
    solution = [[0 for _ in range(9)] for _ in range(9)]
    for (row, col), color in coloring.items():
        solution[row][col] = color + 1  # Colors are zero-indexed, so add 1 to map to Sudoku numbers
    
    return solution

# Function to print the Sudoku grid
def print_sudoku(sudoku):
    for row in sudoku:
        print(" ".join(str(num) if num != 0 else "." for num in row))

# Example Sudoku puzzle (0 represents empty cells)
sudoku = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
#sudoku = [
#    [0, 0, 3, 0, 2, 0, 6, 0, 0],
#    [9, 0, 0, 3, 0, 5, 0, 0, 1],
#    [0, 0, 1, 8, 0, 6, 4, 0, 0],
#    [0, 0, 8, 1, 0, 2, 9, 0, 0],
#    [7, 0, 0, 0, 0, 0, 0, 0, 8],
#    [0, 0, 6, 7, 0, 8, 2, 0, 0],
#    [0, 0, 2, 6, 0, 9, 5, 0, 0],
#    [8, 0, 0, 2, 0, 3, 0, 0, 9],
#    [0, 0, 5, 0, 1, 0, 3, 0, 0]
#]

# Solve the Sudoku
solution = solve_sudoku(sudoku)

# Print the solved Sudoku
print("Solved Sudoku:")
print_sudoku(solution)

