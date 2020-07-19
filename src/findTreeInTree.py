from collections import deque

class Node(object):
    def __init__(self, value: int, left, right):
        self.Value = value
        self.Left = left
        self.Right = right

def findTreeInTree(root: Node, node: Node) -> bool:
    q = deque()
    q.append(root)
    while len(q) > 0:
        cNode = q.popleft()
        
        if cNode is None: continue

        if cNode.Value == node.Value and compareTrees(cNode, node):
            return True

        q.append(cNode.Left)
        q.append(cNode.Right)
    return False

def compareTrees(node1: Node, node2: Node) -> bool:
    if node1 == node2 == None: return True

    if node1 is not None and node2 is not None:
        if node1.Value != node2.Value: return False 
        return compareTrees(node1.Left, node2.Left) and compareTrees(node1.Right, node2.Right)
    return False