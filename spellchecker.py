#importing the needed libraries

from textblob import TextBlob
from textblob.en import split

# importing the text
inputText = input('Input a sentence: ')
# splitting the words
words = inputText.split(' ')
#counting the number of words
count = len(words)
#going through each word
for num in range (count):
    check = TextBlob(words[num])
#correcting each word
    corrected = str(check.correct())
    
    if not check == corrected:
        print('Did you mean '+ corrected + ' ?')
