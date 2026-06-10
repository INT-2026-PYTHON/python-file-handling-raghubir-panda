"""
## 5. Longest Palindrome in the File  *(Hard)*

=================================================
LONGEST PALINDROME
=================================================

Problem Statement:
Read the text file `sowpods.txt` and find the
LONGEST PALINDROME word in the file.

If multiple palindromes share the maximum
length, print ALL of them.

-------------------------------------------------
Input Example (sowpods.txt sample):
level
radar
noon
civic
deified
racecar
rotator
malayalam

Output Example:
Longest palindrome length: 9
malayalam

-------------------------------------------------
Explanation:
Lengths of the palindromes in the sample:
   level    -> 5
   radar    -> 5
   noon     -> 4
   civic    -> 5
   deified  -> 7
   racecar  -> 7
   rotator  -> 7
   malayalam -> 9
The longest is "malayalam" with 9 characters.
=================================================

"""
longest_palindromes = []
max_length = 0

with open("file_reading_practice/sowpods.txt") as file:
    for word in file:
        word = word.strip().lower()
        if word == word[::-1] and len(word) > 0:
            length = len(word)
            if length > max_length:
                max_length = length
                longest_palindromes = [word]
            elif length == max_length:
                longest_palindromes.append(word)

print(f"Longest palindrome length: {max_length}")
for palindrome in longest_palindromes:
    print(palindrome)