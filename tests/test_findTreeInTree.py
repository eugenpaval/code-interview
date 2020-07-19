import unittest
from src.findTreeInTree import Node, findTreeInTree

class FindTreeInTreeTestSuite(unittest.TestCase):
    tree1 = \
    [
        Node(10, 1, 2),
        Node(5, 3, 4),
        Node(-3, None, 5),
        Node(3, 6, 7),
        Node(2, None, 8),
        Node(11, None, None),
        Node(3, None, None),
        Node(-2, None, None),
        Node(1, None, None),
        Node(5, None, None)
    ]

    tree2 = \
    [
        Node(3, 1, 2),
        Node(3, None, None),
        Node(-2, None, None)
    ]

    def buildtree(self, tree):
        for node in tree:
            node.Left = tree[node.Left] if node.Left is not None else None
            node.Right = tree[node.Right] if node.Right is not None else None
        return tree[0]

    def test1(self):
        t1 = self.buildtree(FindTreeInTreeTestSuite.tree1)
        t2 = self.buildtree(FindTreeInTreeTestSuite.tree2)
        self.assertEqual(findTreeInTree(t1, t2), True)