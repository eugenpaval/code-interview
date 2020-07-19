from functools import reduce
def generateParens(count):
    pList = []
    pStr = [None] * count * 2 
    addParens(pList, count, count, pStr, 0)

    return pList

def addParens(pList, countL, countR, pStr, index):
    if countL < 0 or countR < countL: return

    if countL == 0 and countR == 0:
        pList.append(reduce(lambda a,b: a+b, pStr, initial = ""))
    else:
        pStr[index] = "("
        addParens(pList, countL-1, countR, pStr, index+1)
        pStr[index] = ")"
        addParens(pList, countL, countR-1, pStr, index+1)
