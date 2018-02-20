"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    hc = False
    node = head
    nodeList = []
    while (node != None):
        if (nodeList.count(node) != 0):
            hc = True
            break
        nodeList.append(node)
        node = node.next
    return(hc)
    
