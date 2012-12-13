alphabet=['A','B','C']

def wirth(n):
    solutions=[]
    if n==0:
        return []
    if n==1:
        return alphabet
    
    for prev in wirth(n-1):
        
        for letter in alphabet:
            if letter==prev[-1]:
                continue
            current = prev+letter
            if isWirth(current):
                solutions.append(current)
    # print solutions
    return solutions

def isWirth(l):
    
    for i in range(1, (len(l)/2)+1):
        if l[-i:] == l[-i*2:-i]:
            return False
    return True;
