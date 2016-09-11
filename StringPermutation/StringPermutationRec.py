
 # String Permutation

def strpermute(s):
    
    permlist = []
    
    if len(s) == 1:
        permlist = [s]  # return single character as it does not have more combination
    
    for i in range(len(s)):
        
        # get all the letters one by one
        for comb in strpermute(s[:i] + s[i+1:]): 
            
            # Call function on the remaining characters other than first letter
            # and keep doing until one letter left
            permlist.append(s[i] + comb) # append new permutation to permlist
            
    return permlist # return all permutations


s = "abcd"

l = strpermute(s)

print(l)



