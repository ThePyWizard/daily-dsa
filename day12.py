#check for balanced expression

def is_balanced(expression):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack.pop() != closing_brackets[char]:
                return False

    return len(stack) == 0

expression1 = input("Enter the expression : ")
print(f"Expression '{expression1}' is balanced: {is_balanced(expression1)}")

