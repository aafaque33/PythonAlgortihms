# **N! ( Factorial of  n )**

def nfactorial(n):
    if(n==0):
        return 1
    
    # if n not equal zero call funtion again for n-1 as n! = n * (n-1)!
    fac = n * nfactorial(n-1)
    
    return(fac)


nfactorial(5)
