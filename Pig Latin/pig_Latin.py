# English to Pig Latin
print('Enter the english sentence to translate into Pig-Latin')

message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = []       # A list of pig latin words
for word in message.split():
    
    # separate non-letters from the beginning of the word list
    prefixNonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonletters += word[0]
        word = word[1:]
    
    if len(word) == 0:
        pigLatin.append(prefixNonletters)
        continue
    
    # separate non-letters from the end of the word list
    suffixNonletters = ''
    while not word[-1].isalpha():
        suffixNonletters += word[-1]
        word = word[:-1]
    
    # check if the word is in uppercase or titlecase
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower() # Make the word in lowercase

    prefixConsonants = ''
    while len(word)>0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the word
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    
    # set the word back to uppercase or titlecase
    if wasUpper:
        word = word.upper()
    
    if wasTitle:
        word = word.title()

    # Add the non-letters back to the start or end of the word 
    pigLatin.append(prefixNonletters+word+suffixNonletters)

# Join all the words back to a single string
print(' '.join(pigLatin))