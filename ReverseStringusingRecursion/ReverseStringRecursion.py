
# Reverse a String using Recursion

def reverse(S):
    # If only one character left return it
    if len(S) == 1:
        return S
    
    # concat the first character at every step with returned character from recrsion
    revstr = reverse(S[1:]) + S[0]
    
    return(revstr)


reverse("I Love Programming in Python")
