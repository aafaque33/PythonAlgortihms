

def balance_check(s):
    
    stack = [];
    
    par = ['(','{','[']
    
    for char in s:
        
        if char in par:
            stack.append(char)
            
        else:
            if len(stack) == 0:
                return False
            
            else:
                recopen = stack.pop()
                
                if recopen == '(':
                    if char != ')':
                        return False
                if recopen == '{':
                    if char != '}':
                        return False
                if recopen == '[':
                    if char != ']':
                        return False
    if len(stack) == 0:
        return True
    else:
        return False


print(balance_check('([]{})'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))



