# mini name-database
# You ask for a word. You display:
# number of vowels
# number of consonants
# if it has spaces → error
# You use:
# for
# conditions
# functions

vocals = ["a", "e", "i", "o", "u"]
consonants = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
    "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"
]
word_vocals=[]
word_consonants=[]
vowels_no=0
consonant_no=0

user_word=input("Please add the word to be splitted in vocals and consonants:\n")

for i in user_word:
    if i in vocals:
        word_vocals.append(i)
        vowels_no+=1
    elif i in consonants:
        word_consonants.append(i)
        consonant_no+=1
    else:
        print(f"{i} is not a valid letter")


print(f" the vowel letters from the word {user_word} are {",".join(word_vocals)} with a total number of {vowels_no} and the consonants letters are {",".join(word_consonants)} with a total number of {consonant_no}")
