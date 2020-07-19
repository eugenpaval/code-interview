#%%
def makeChange(amount):
    denoms = [25, 10, 5, 1]
    map = [[None] * len(denoms) for _ in range(amount + 2)]
    return makeChangeHelper(amount, denoms, 0, map)

def makeChangeHelper(amount, denoms, index, map):
    if map[amount][index] is not None: return map[amount][index]
    if index >= len(denoms) - 1: return 1

    count = i = 0
    denomAmount = denoms[index]
    while i * denomAmount <= amount:
        remAmount = amount - i * denomAmount
        count += makeChangeHelper(remAmount, denoms, index + 1, map)
        i += 1
    map[amount][index] = count

    return count

print(makeChange(100))

# %%
