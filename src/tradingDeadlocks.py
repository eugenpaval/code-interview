class LockNode(object):
    def __init__(self, id = None):
        self.ID = id
        self.Edges = {}

    def findDeadLock(self, followedPath, visitedNodes, retVal):
        if self in visitedNodes:  return True

        for p, n in self.Edges.items():
            thisPathDeadLocked = False

            currentPath = followedPath + [p]
            thisPathDeadLocked = n.findDeadLock(currentPath, visitedNodes + [self], retVal)
            if thisPathDeadLocked: retVal.append([k for k in currentPath])

        return False

def contains(array, subArray):
    if len(array) == 0: return False
    
    contained = False
    for i in range(len(array)):
        if len(array[i]) != len(subArray): return False
        contained = True
        for j in range(len(subArray)):
            if array[i][j] != subArray[j]:
                contained = False
                break
        
    return contained

def scrub(result):
    result, retVal = sorted(result), []
    for array in result:
        scrubbed = []
        array = sorted(array)
        i = 0
        while i < len(array):
            p = array[i]
            scrubbed.append(p)
            i += 1
            while i < len(array) and array[i] == p: i += 1
        
        retVal.append(scrubbed)

    for i in range(len(retVal)-1, -1, -1):
        a = retVal[i]
        for b in filter(lambda x: len(x) < len(a), retVal):
            c = [k for k in b if k in a]
            if len(c) > 1: retVal[i] = c

    return map(lambda x: tuple(x), retVal)

def buildGraph():
    allLocks, allPaths = {}, set()
    pNode = None
    for path, locks in pathsWithLocks.items():
        allPaths.add(path)
        for l in locks:
            if l not in allLocks:
                allLocks[l] = LockNode(l)
            node = allLocks[l]
            if pNode is not None:
                pNode.Edges[path] = node
            pNode = node
        pNode = None
    return (allPaths, allLocks)

def findDeadLocks(pathsWithLocks):
    allPaths, allLocks = buildGraph()
    deadLocks = set()

    for path in sorted(allPaths):
        for n in map(lambda l: allLocks[l], pathsWithLocks[path]):
            retVal = []

            n.findDeadLock([path], [], retVal)
            if len(retVal) > 0:
                r = scrub(retVal)
                for d in r:
                    deadLocks.add(d)

    return sorted(sorted(deadLocks), key = lambda x: len(x))

pathsWithLocks = \
{
    # 'UseCase1': ['Lock0','Lock1','Lock2'],
    # 'UseCase2': ['Lock1','Lock2'],
    # 'UseCase3': ['Lock4','Lock2','Lock1'],
    # 'UseCase4': ['Lock2','Lock1']
    
    # UseCase1,UseCase2
    # UseCase1,UseCase4
    # UseCase2,UseCase3
    # UseCase3,UseCase4

    'UseCase1': ['Lock7', 'Lock8', 'Lock6', 'Lock1'], 
    'UseCase2': ['Lock4', 'Lock6', 'Lock5', 'Lock2'], 
    'UseCase3': ['Lock3', 'Lock5', 'Lock8', 'Lock9'], 
    'UseCase4': ['Lock7', 'Lock9', 'Lock4', 'Lock1'], 
    'UseCase5': ['Lock3', 'Lock2']
}

print(findDeadLocks(pathsWithLocks))