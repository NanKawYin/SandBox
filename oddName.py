"""NanKawYin"""

name = str(input("Enter Your Name: "))
name_count = len(name)
while name_count == 0:
    print("User name cannot be empty.")
    name = input("Enter Your Name: ")
print(name[0:name_count+1:2])
