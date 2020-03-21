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

class Final(Node):
    steps = 0
    def IsSuccess(self):
        return self.cost == 0

def make_final(board, steps):
    final = Final()
    final.board = board
    final.cost = evaluate(board)
    final.steps = steps
    return final

def find_best_successor(successors):
    best = Node()
    
    for successor in successors:
        if (evaluate(successor) < best.cost):
            best = make_node(successor)

    return best

def climb(problem):
    current = make_node(problem)
    steps = 0
    while (1):
        steps += 1
        neighbor = find_best_successor(
            generate_successors(current.board))
        if (neighbor.cost >= current.cost):
            return make_final(current.board, steps)
        current = neighbor