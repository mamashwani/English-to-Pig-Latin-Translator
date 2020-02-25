# -*- coding: utf-8 -*-
"""
Muhammad Mashwani
PeopleSoft ID: 1378052
Assignment #5

"""

def is_vowel(letter):
    return letter.upper() in 'AEIOU' # if the letter is a vowel return True

def has_vowel(word):
    for letter in word: 
        # Loop through all the letters
        if is_vowel(letter):
            # See if a letter is a vowel
            return True # If so, return True, "has a vowel" is True
                        # After looking through all the letters in the word
    return False 
                # we found no vowel, so the word does not have a vowel

def vowel_index(word):
    index = 0
    for letter in word:
        if is_vowel(letter):
            return index
        index += 1
    return -1
        
def is_first_letter_capital(word):
    return word[0].isupper()



def translate(word):  
    if is_vowel(word[0]): 
        # The word starts with a vowel (Rule #1)
        # add way to the end of the word
        return word + 'way'
    elif has_vowel(word): 
        # The word must have a vowel that is not the first letter (Rule #3)
        # ToDo: Fix this
        index = vowel_index(word)
        if is_first_letter_capital(word):
            new_word = word.lower()
            return new_word[index:].capitalize() + new_word[:index] + 'ay'
        else:
            return word[index:] + word[:index] + 'ay'
    else:
        #the word has no vowels (Rule #2) 
        return word + 'way'

print("This program will translate a word from English to Pig Latin.")

choice = 'Y'
while choice.upper() == 'Y': #Loop as long as the user says Yes
    word = input("Please enter a word: ")
    print(word, "becomes", translate(word))
    choice = input("Would you like another word? (Y/N) ")

print("Ankthay ouyay!")