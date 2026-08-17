s = "mol"

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
m="level"
left=0
right=len(m)-1
while left<right:
    if m[left] != m[right]:
        print("not palindrome")
        break
    left +=1
    right -=1
else:
    print("palindrome")
