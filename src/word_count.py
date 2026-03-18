from collections import defaultdict

def wordCount(document):
    str = ""
    for i in document:
        if i.isalpha() or i == " ":
            str += i.lower()
    x = str.split()
    #print(x)
    dict = defaultdict(list)
    for i in x:
        dict[i] += 1
    print(dict)
    
    

    


document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"
 #output = [ ["practice", "3"], ["perfect", "2"],["makes", "1"], ["youll", "1"], ["only", "1"], ["get", "1"], ["by", "1"], ["just", "1"] ]
 
wordCount(document)