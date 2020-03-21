from evaluate import *
from generate_nxn import *

class Node:
    board = []
    cost = float("inf")

def make_node(board):
    node = Node()
    node.board = board
    node.cost = evaluate(board)
    return node

def find_best_successor(successors):
    best = Node()
    
    for successor in successors:
        if (evaluate(successor) < best.cost):
            best = make_node(successor)

    return best

def climb(problem):
    current = make_node(problem)
    while (1):
        neighbor = find_best_successor(
            generate_successors(current.board))
        if (neighbor.cost >= current.cost):
            return current.board
        current = neighbor