def count_vowel(string):
    vowels = {"a", "e", "i", "o", "u"}
    count = 0

    string = string.lower()

    for char in string:
        if char in vowels:
            count += 1

    return count


input_string = str(input("Enter any string to count vowerls="))
vowel_count = count_vowel(input_string)
print(f"The number of vowels in the sting '{input_string}'  is {vowel_count}")
