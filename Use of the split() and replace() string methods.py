s = input("Enter a sentence: ")
print("Words: ", s.split())

old = input("Enter a word to replace: ")
new = input("Enter the new word: ")
s = s.replace(old, new)

print("Modified sentence: ", s)