def evaluate(solution): 
    target = list("Hello, World!") 
    diff = 0
    for i in range(len(target)): 
        s = solution[i] 
        t = target[i] 
        diff += abs(ord(s) - ord(t)) 
    return diff 