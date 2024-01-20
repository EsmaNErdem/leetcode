def isValid(s):
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for p in s:
        if p in bracket_pairs:
            stack.append(p)
        elif not stack or bracket_pairs[stack.pop()] != p:
            return False
        
    return len(stack) == 0
