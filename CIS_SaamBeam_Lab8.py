# Saam Beam
# oct 14, 2024
# CIS Lab 8 - Palindromes

word = input("Type in a word that may or may not be a palindrome: ").lower()

def is_palindrome():
    word_compare = []
    word_compare.append(word)
    
    reverse_word_compare = word[::-1]


    if reverse_word_compare == word:
        print("Your word is a palindrome")
    else:
        print("Your word is not a palindrome")




is_palindrome()