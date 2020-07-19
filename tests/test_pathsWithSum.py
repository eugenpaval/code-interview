import unittest
from src.PathsWithSum import Node, countPathsWithSum, cPS

class PathsWithSumTestSuite(unittest.TestCase):
    tree = \
    [
        Node((10, [1,2])),
        Node((5, [3,4])),
        Node((-3, [None,5])),
        Node((3, [6,7])),
        Node((2, [None,8])),
        Node((11, [None,None])),
        Node((3, [None,None])),
        Node((-2, [None,None])),
        Node((1, [None,None])),
        Node((5, [None,None]))
    ]

    def buildtree(self, tree):
        for node in tree:
            node.Left = tree[node.Left] if node.Left is not None else None
            node.Right = tree[node.Right] if node.Right is not None else None
        return tree[0]

    def test1(self):
        Tree = self.buildtree(PathsWithSumTestSuite.tree)
        self.assertEqual(countPathsWithSum(Tree, 8), 3)

    def test2(self):
        Tree = self.buildtree(PathsWithSumTestSuite.tree)
        self.assertEqual(cPS(Tree, 8, 0, {}), 3)