class QueueusingStacks(object):
    
    def __init__(self):
        
        # Inititialize 2 stacks
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,item):
        # append item to stack1 for enqueue
        self.stack1.append(item)
        
    def dequeue(self):
        
        # Check if Stack 2 is empty then pop all items from stack 1 and append in stack 2 and finally pop from Stack2
        # Else keep poping from stack2 until its not empty ( repeat first step if empty )
        
        if self.stack2 == []:
            while not self.stack1 == []: 
                self.stack2.append(self.stack1.pop())
                
        return self.stack2.pop()
