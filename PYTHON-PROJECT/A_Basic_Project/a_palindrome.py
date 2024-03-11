def palindrome(s):
    return s == s[::-1]


word = str(input("Enter a word: "))

if palindrome(word):
    print(f"{word} is a palindrome.")

else:
    print(f"{word} is not palindrome")
