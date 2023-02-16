
testcases = int(input())

def is_var(word):
    return word[0] == "<"

def algo(phrase1, phrase2): 
    for i in range(len(phrase1)):
        word1 = phrase1[i]
        word2 = phrase2[i]

        if word1 != word2 and is_var(word1):
            phrase1 = [word2 if w == word1 else w for w in phrase1] 

        elif word1 != word2 and is_var(word2):
            phrase2 = [word1 if w == word2 else w for w in phrase2] 

        elif word1 != word2 and not is_var(word1) and not is_var(word2):
            return "-"
    
    for i in range(len(phrase1)):
        word1 = phrase1[i]
        word2 = phrase2[i]
        if is_var(word1) != is_var(word2):
            return algo(phrase1, phrase2)
    return " ".join("w" if is_var(w) else w for w in phrase1)

for _ in range(testcases):
    phrase1 = input().split()
    phrase2 = input().split()
    print(algo(phrase1, phrase2))