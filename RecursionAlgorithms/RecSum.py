# Write a recursive function which takes an integer and computes the cumulative sum of 0 to that integer
# 
# For example, if n=4 , return 4+3+2+1+0, which is 10.


def rec_sum(n):
    if(n==1):
        return 1
    
    # If n == 1 return else sum = n + sum(n-1)
    sum = n + rec_sum(n-1)
    
    return(sum)


rec_sum(10)

