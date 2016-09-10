# Given an integer, create a function which returns the sum of all the individual digits in that integer. For example: if n = 4321, return 4+3+2+1


def sum_ind_digits(n):
    
    # return n If only n is 1 digit left as e.g 1 % 10 or 9%10 is always 1 and 9 respectively
    if((n % 10) == n):
        return n
    
    # sum the single digit with recursing passing rest digit in functions again
    # 4321 % 10 = 1  and 4321 / 10 = 432
    sum = ( n % 10 ) + sum_ind_digits(n//10)
    
    return(sum)


sum_ind_digits(54321)

