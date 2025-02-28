from itertools import count


def pangram(s):
    if len(set(s)) == 26:
        return True
    return False

s = "leetcode" #--> True
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(pangram(s))
#print(pangram(sentence))