
class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


def nth_to_last_node(n, head):
    firstnode = head
    secondnode = head
    
    for i in range(n-1):
        firstnode = firstnode.nextnode
        
    while firstnode.nextnode:
        firstnode = firstnode.nextnode
        secondnode = secondnode.nextnode
        
    return(secondnode)
