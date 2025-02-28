from collections import defaultdict
def areOccurrencesEqual(s):
    map = defaultdict(int)
    for x in s:
        map[x] += 1
    
    frequencies = map.values()
    return sum(frequencies) % 2 == 0


s = "abacbc"
print(areOccurrencesEqual(s))