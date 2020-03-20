from evaluate import *

class Node:
    board = []
    cost = 10000

print(Node())

def find_best_successor(successors):
    best = Node()
    
    for successor in successors:
        if (evaluate(successor) < best.cost):
            best.board = successor
            best.cost = evaluate(successor)

    return best