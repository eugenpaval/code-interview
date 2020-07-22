def arrange(input):
    result = []
    counter = CountingSet(input)

    c = None
    while True:
        c = counter.useMaxChar(c)
        
        if c is None:
            if not counter.isEmpty(): return ""
            break

        result.append(c)

    return "".join(result)

class Counter(object):
    def __init__(self, char, count):
        self.Char = char
        self.Count = count
        self.Next = None

class CountingSet(object):
    def __init__(self, input):
        self.SortedSet = None
        self.count(input)

    def count(self, input):
        d = {}
        for c in input:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        
        for char, count in sorted(d.items(), key = lambda e: e[1], reverse = True):
            if self.SortedSet is None:
                self.SortedSet = node = Counter(char, count)
            else:
                node.Next = Counter(char, count)
                node = node.Next

    def useMaxChar(self, pChar):
        if self.SortedSet is None: return None
        
        head = self.SortedSet if self.SortedSet.Char != pChar else self.SortedSet.Next

        if head is None: return None

        retVal = head.Char
        newHead = self.decCount(head)
        if self.SortedSet == head:
            self.SortedSet = newHead
        else:
            self.SortedSet.Next = newHead 
                
        return retVal

    def isEmpty(self):
        return self.SortedSet is None

    def decCount(self, head):
        head.Count -= 1
        if head.Count == 0:
            return head.Next

        cNode = head
        while cNode.Next is not None and head.Count < cNode.Next.Count:
            cNode = cNode.Next
        if head != cNode:
            cNode.Next, head.Next, head = head, cNode.Next, head.Next

        return head

print(arrange("abacuieabbceaa"))
