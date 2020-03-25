import random
from evaluate import *
from generate_nxn import *

class Node:
    moves = [] # all of the moves 
    board = []
    cost = float("inf")
    def AddMove(self, state):
        self.moves.append(state)

def make_node(board):
    node = Node()
    node.board = board
    node.cost = evaluate(board)
    return node

class Final(Node):
    steps = -1
    sideways = -1
    restarts = -1
    def IsSuccess(self):
        return self.cost == 0

def make_final(board, steps, moves):
    final = Final()
    final.board = board
    final.cost = evaluate(board)
    final.steps = steps
    final.moves = moves
    return final

def find_best_successor(successors):
    best = Node()
    
    for successor in successors:
        if (evaluate(successor) < best.cost):
            best = make_node(successor)

    return best

def find_random_successor(successors):
    index = random.randint(0, len(successors) - 1)
    return make_node(successors[index])

def climb(problem, limit = 100000):
    current = make_node(problem)
    steps = 0
    moves = []
    while (1):
        steps += 1
        moves += [current.board]
        neighbor = find_best_successor(
            generate_successors(current.board))
        if (neighbor.cost >= current.cost or steps >= limit):
            return make_final(current.board, steps, moves)

        current = neighbor

def climb_outside(
    problem, 
    max_count, 
    method_to_call, 
    method_amount, 
    attribute_count_name
):
    count = 0
    current  = climb(problem)
    steps = current.steps
    sideways = current.sideways
    restarts = current.restarts
    moves = current.moves
    while(count < max_count):
        current = method_to_call(current, method_amount)
        steps += current.steps
        moves += current.moves
        if (current.sideways > -1):
            sideways += current.sideways
        if (current.IsSuccess()):
            break
        count += 1
    final = make_final(current.board, steps, moves)
    if (current.sideways > -1):
        final.sideways += sideways
    setattr(final, attribute_count_name, count)
    return final

##### SIDWAYS #####
def climb_sideways_outside_call(node, amount):
    return climb(
        find_random_successor(
            generate_sideways_successors(node.board)
        ).board,
        amount
    )

def climb_sideways(problem, sideways_moves):
    return climb_outside(
        problem, 
        sideways_moves, 
        climb_sideways_outside_call, 
        100,
        'sideways'
    )
##### SIDWAYS END #####

##### RANDOM RESTART #####
def climb_random_restart_outside_call(node, amount):
    return climb(
        generate_initial_state(len(node.board)),
        amount
    )

def climb_random_restart(problem, restarts):
    return climb_outside(
        problem, 
        restarts, 
        climb_random_restart_outside_call, 
        100, # Limit the number of climbs to 100 before restarting
        'restarts'
    )
##### RANDOM RESTART END #####

##### RANDOM RESTART SIDEWAYS #####
def climb_random_restart_sideways_outside_call(node, amount):
    return climb_sideways(
        generate_initial_state(len(node.board)),
        amount
    )

def climb_random_restart_sideways(problem, restarts):
    return climb_outside(
        problem, 
        restarts, 
        climb_random_restart_sideways_outside_call, 
        10, # Limit of 10 sideways moves before restarting
        'restarts'
    )
##### RANDOM RESTART SIDEWAYS END #####
