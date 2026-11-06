# Write a program to remove duplicate characters from a string. 

s = input("Enter a string: ")
ns = ""
for i in s:
    if i not in ns:
        ns+=i
print("string after removing duplicates:", ns)
    


