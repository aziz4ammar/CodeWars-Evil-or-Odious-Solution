def evil(n):
    binary = bin(n)[2:]
    return "It's Evil!" if binary.count('1') % 2 == 0 else "It's Odious!"