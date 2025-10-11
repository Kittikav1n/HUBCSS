def parentheses(s: str):
    stack = []
    mapping = { ")" : "(" , "}" : "{" , "]" : "["}
    for char in s:
        if char in mapping:
            element = stack.pop() if stack else "#"
            if mapping[char] != element:
                return False
        else :
            stack.append(char)
    return not stack
    
print(f": {parentheses('()')}")
print(f": {parentheses('()[]{}')}")