class Box(object):
    def __init__(self, h, w, d):
        self.Height = h
        self.Width = w
        self.Depth = d

    def __gt__(self, other):
        return self.Height - other.Height

    def canBeAbove(self, other):
        return self.Height > other.Height and self.Width > other.Width and self.Depth > other.Depth

def createStack(boxes):
    boxes.sort(reverse = True)
    stackMap = [None] * len(boxes)
    return createStackHelper(boxes, None, 0, stackMap)

def createStackHelper(boxes, bottomBox, offset, stackMap):
    if offset >= len(boxes): return 0

    newBottomBox = boxes[offset]
    heightWithBottom = 0
    if bottomBox is None or newBottomBox.canBeAbove(bottomBox):
        if stackMap[offset] is None:
            stackMap[offset] = createStackHelper(boxes, newBottomBox, offset+1, stackMap)
            stackMap[offset] += newBottomBox.Height
        heightWithBottom = stackMap[offset]

    heightWithoutBottom = createStackHelper(boxes, bottomBox, offset+1, stackMap)
    return max(heightWithBottom, heightWithoutBottom)