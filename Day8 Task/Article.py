# A writer saves an article in a file called article.txt. Write a Python program that opens and reads the file, counts the number of words, lines, and characters in the file, and displays the results.
 
# Read the whole file into one string
with open("article.txt", "r") as f:
    text = f.read()
 
print("Words:", len(text.split()))        # split() breaks text into words
print("Lines:", len(text.splitlines()))   # splitlines() breaks text into lines
print("Characters:", len(text))           # length of the text = characters
