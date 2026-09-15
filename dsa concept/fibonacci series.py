def febonacci(n):
    if n==0 or n==1:
        return n
    return febonacci(n-1)+febonacci(n-2)
print(febonacci(4))
#Tribonacci Series
def tri(j):
    if j==0 or j==1:
        return j
    if j==2:
        return 1
    return tri(j-1)+tri(j-2)+tri(j-3)
print(tri(8))

def fec(n):
    if n==0:
        return 1
    return n*fec(n-1)
print(fec(5))
def reverse_word(s):
    # Base Case
    if s == "":
        return ""
    
    # s[0] matlab pehla letter, s[1:] matlab baaki bacha word
    return reverse_word(s[1:]) + s[0]

print(reverse_word("cat"))
