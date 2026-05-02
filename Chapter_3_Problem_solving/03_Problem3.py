#3.Write a program to detect double space in a string

Name = "My Name Is Foram Shah.  "
#if we get -1 in output means no whitespace found.
result = Name.find("  ")
print(f"Index of double space: {result}")