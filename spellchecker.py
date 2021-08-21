
from textblob import TextBlob
from textblob.en import split

inputText = input('Input a sentence: ')
words = inputText.split(' ')
count = len(words)

for num in range (count):
    check = TextBlob(words[num])
    corrected = str(check.correct())
    
    if not check == corrected:
        print('Did you mean '+ corrected + ' ?')