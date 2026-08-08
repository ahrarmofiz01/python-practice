student={"name": "ahrar","age":20,"gender":"male"}
print(student["age"])
student["name"]="john"
student["age"]=21
student["gender"]="male"
print(student)
if "john" in student["name"]:
    print(True)
print(student.get("Ali"))#if kew is not present then it will  return None