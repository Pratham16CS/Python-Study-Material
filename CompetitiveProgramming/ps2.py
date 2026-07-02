def is_anagram(A,B):
    if (len(A) != len(B)):
        return "NO"
    
    char_count = {}
    for char in A:
        char_count[char] = char_count.get(char,0) + 1 
    

    for char in B:
        if char not in char_count:
            return "NO"
        
        char_count[char] -= 1
        if char_count[char] < 0:
            return "NO"
        
        
    return "YES"

T = int(input())
for i in range(T):
    A = input()
    B = input()
    anagram = is_anagram(A,B)
    print(anagram)