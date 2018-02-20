""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    bst = True
    nodeList = [root]
    dataList = []
    pointer = 0
    while (pointer < len(nodeList)):
        node = nodeList[pointer]
        data = node.data
        if (dataList.count(data) > 0):
            bst = False
            break
        dataList.append(data)
        # Find Max of left subtree
        left = node.left
        if (left != None):
            nodeList.append(left)
            leftSubtree = [left]
            leftPointer = 0
            maxLeftData = left.data
            while (leftPointer < len(leftSubtree)):
                if (leftSubtree[leftPointer].left != None):
                    leftSubtree.append(leftSubtree[leftPointer].left)
                if (leftSubtree[leftPointer].right != None):
                    leftSubtree.append(leftSubtree[leftPointer].right)
                leftPointer = leftPointer + 1
            for i in range(len(leftSubtree)):
                if (maxLeftData < leftSubtree[i].data):
                    maxLeftData = leftSubtree[i].data
            if (maxLeftData > data):
                bst = False
                break
        # Find Min of right subtree
        right = node.right
        if (right != None):
            nodeList.append(right)
            rightSubtree = [right]
            rightPointer = 0
            minRightData = right.data
            while (rightPointer < len(rightSubtree)):
                if (rightSubtree[rightPointer].left != None):
                    rightSubtree.append(rightSubtree[rightPointer].left)
                if (rightSubtree[rightPointer].right != None):
                    rightSubtree.append(rightSubtree[rightPointer].right)
                rightPointer = rightPointer + 1
            for i in range(len(rightSubtree)):
                if (minRightData > rightSubtree[i].data):
                    minRightData = rightSubtree[i].data
            if (minRightData < data):
                bst = False
                break
        pointer = pointer + 1
    return (bst)