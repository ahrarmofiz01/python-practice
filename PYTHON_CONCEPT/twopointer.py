word="level"
left=0
right=len(word)-1
while left<right:
    if word[left]==word[right]:
        print("word is pelendrome")
    left=left+1
    right=right-1