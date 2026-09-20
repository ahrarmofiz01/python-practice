#LONGEST SUBSTRING WITHOUT REPEARTING CHARACTERS
s="abcabcdab"
n = len(s)

if n <= 1:
    print(n)
else:
    set1 = set()
    i, j = 0, 0  
    ans = 0

    while j < n:
        while s[j] in set1:
            set1.remove(s[i])
            i += 1
        set1.add(s[j])
        ans = max(ans, j - i + 1)
        j += 1

    print(ans)
print(10)
