from collections import Counter

def ransom_note(magazine, ransom):
    m = Counter(w for w in magazine)
    r = Counter(w for w in ransom)

    for key in r:
        if not ((key in m) and (m[key] >= r[key])):
            return False
    return True

if __name__ == '__main__':
    m, n = map(int, input().strip().split(' '))
    magazine = input().strip().split(' ')
    ransom = input().strip().split(' ')
    answer = ransom_note(magazine, ransom)
    if(answer):
        print("Yes")
    else:
        print("No")
