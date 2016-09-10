
# coding: utf-8

# # Nth to the Last Node
# 
# ## Problem Statement
# 
# Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list. For example, given:
# 
# ## Solution

# In[2]:

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


# In[3]:

def nth_to_last_node(n, head):
    firstnode = head
    secondnode = head
    
    for i in range(n-1):
        firstnode = firstnode.nextnode
        
    while firstnode.nextnode:
        firstnode = firstnode.nextnode
        secondnode = secondnode.nextnode
        
    return(secondnode)


# # Test Cases using Nose tools

# In[5]:

"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(2,a),d)
        print('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)


# In[ ]:



