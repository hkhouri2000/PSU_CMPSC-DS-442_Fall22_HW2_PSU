############################################################
# CMPSC 442: Homework 2
############################################################

student_name = "Type your full name here."

############################################################
# Imports
############################################################

from math import factorial
from itertools import permutations
from random import random 
# Usable imports: collections, itertools, math, random 



############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
    # We are taking n placements on a grid with (n x n) possible positions 
    return factorial(n * n) // factorial(n) // factorial(n * n - n)

def num_placements_one_per_row(n):
    # For each row, a queen can be placed in n! ways. We multiply with the
    # number of rows to get the total number of placements. 
    return n * factorial(n)

def n_queens_valid(board):
    # Check all possible pairs of queens
    for i in range(len(board)):
        for j in range(len(board)):
            # Do not compare queen to itself
            if i == j:
                continue 

            # Check if two queens are at the same column
            if board[i] == board[j]:
                return False 
            
            # If the difference in row is the same as the difference in column,
            # then the two queens must be on the same diagonal 
            if abs(i - j) == abs(board[i] - board[j]):
                return False

    return True 

def n_queens_solutions(n):
    # Create all permutations and test each if it is valid 
    for comb in permutations(range(n), n):
        if n_queens_valid(comb):
            yield list(comb)

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):

    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass

def create_puzzle(rows, cols):
    pass

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
    pass

def solve_distinct_disks(length, n):
    pass

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
