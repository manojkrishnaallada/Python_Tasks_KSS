#Write a program to find the student with the highest marks from a dictionary. 

d = {"Manoj": 95, "Krishna": 85, "Chintu": 65}
print(max(d, key=d.get))
