def partition(input, dict):
    if len(input) == 0: return False
    if input in dict: return True

    index = len(input) - 1
    while index > 0:
        if partition(input[:index], dict) and partition(input[-index:], dict): return True
        index -= 1

    return False

print(partition("ilikeflower", set(["i", "li", "lik", "like", "flo", "flow", "er"])))