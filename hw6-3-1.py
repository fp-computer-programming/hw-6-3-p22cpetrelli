#author CJP 11/15/2021
word1 = list(input("Enter a word: "))
word2 = list(input("Enter a second word: "))

word1.sort()
word2.sort()

if word1 == word2:
    print("They are anagrams.")
else:
    print("They are not anagrams.")