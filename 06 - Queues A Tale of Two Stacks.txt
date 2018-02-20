class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
        self.queue = []
    
    def peek(self):
        return(self.queue[0])
        
    def pop(self):
        self.queue.pop(0)
        
    def put(self, value):
        self.queue.append(value)

queue = MyQueue()
t = int(raw_input())
for line in xrange(t):
    values = map(int, raw_input().split())
    
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print queue.peek()
        
