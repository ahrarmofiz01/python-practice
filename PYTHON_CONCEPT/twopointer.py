word="level"
left=0
right=len(word)-1
while left<right:
    if word[left]==word[right]:
        print("word is pelendrome")
    left=left+1
    right=right-1
num="123"
left=0
right=len(num)-1
while left<right:
    if num[left]==num[right]:
        print("num is pelindrome")
    else:
        print("not pelendrome")
    left=left+1
    right=right-1