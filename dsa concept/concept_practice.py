array = [0, 5, 7, 2, 9, 8]

largest = array[0]
second = array[1]

for i in array:

    if i > largest:
        second = largest
        largest = i

    elif i > second:
        second = i

print("Largest:", largest)
print("Second Largest:", second)
        
  
