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

def climb_sideways(problem, sideways_moves):
    sideways_count = 0
    current  = climb(problem)
    steps = current.steps
    while(sideways_count < sideways_moves):
        current = climb(find_best_successor(
            generate_sideways_successors(current.board)).board)
        steps += current.steps
        if (current.IsSuccess()):
            break
        sideways_count += 1
    return make_final(current.board, steps)

def climb_random_restart(problem, restarts):
    restart_count = 0
    current  = climb(problem)
    steps = current.steps
    while(restart_count < restarts):
        current = climb(generate_initial_state(len(problem)))
        steps += current.steps
        if (current.IsSuccess()):
            break
        restart_count += 1
    return make_final(current.board, steps)
