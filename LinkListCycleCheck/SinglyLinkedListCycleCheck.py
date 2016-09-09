
class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


def cycle_check(node):
    
    header = node
    
    while(node.nextnode != None):
        if(node.nextnode == header):
            return True
        node = node.nextnode
        
    
    return False

