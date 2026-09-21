#LONGEST SUBSTRING WITHOUT REPEARTING CHARACTERS
s="abcabdab"
n=len(s)
if n<=1:
    print(n)
else:
    i,j=0,0
    set1=set()
    ans=0
    while j<n:
        while s[j] in set1:
            set1.remove(s[i])
            i=i+1
        set1.add(s[j])
        length=j-i+1
        ans=max(ans,length)
        j=j+1
    print(ans)



