class Node(object):
    def __init__(self, nodeRepr) -> None:
        self.Value = nodeRepr[0]
        self.Left = nodeRepr[1][0]
        self.Right = nodeRepr[1][1]

def countPathsWithSum(root, targetSum):
    if root is None: return 0
    
    countFromRoot = countPathsWithSumFromNode(root, targetSum, 0)
    countLeft = countPathsWithSum(root.Left, targetSum)
    countRight = countPathsWithSum(root.Right, targetSum)

    return countFromRoot + countLeft + countRight


def countPathsWithSumFromNode(node, targetSum, currentSum):
    if node is None: return 0

    currentSum += node.Value
    count = 0

    if currentSum == targetSum: count += 1

    count += countPathsWithSumFromNode(node.Left, targetSum, currentSum)
    count += countPathsWithSumFromNode(node.Right, targetSum, currentSum)

    return count

def cPS(node, targetSum, runningSum, pathCount):
    if node is None: return 0

    runningSum += node.Value
    sum = runningSum - targetSum
    totalPaths = pathCount[sum] if sum in pathCount else 0
    
    if sum == 0: totalPaths += 1

    incDict(pathCount, runningSum, 1)
    totalPaths += cPS(node.Left, targetSum, runningSum, pathCount)
    totalPaths += cPS(node.Right, targetSum, runningSum, pathCount)
    incDict(pathCount, runningSum, -1)

    return totalPaths


def incDict(pathCount: dict, runningSum, delta):
    newCount = (pathCount[runningSum] if runningSum in pathCount else 0) + delta

    if newCount == 0:
        del pathCount[runningSum]
    else:
        pathCount[runningSum] = newCount