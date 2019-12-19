userInput = input('enter a string')
if userInput.find('aeiou' or 'AEIOU'):
    lowercase = (userInput.translate({ord(i): None for i in 'aeiouAEIOU'}))
    print(lowercase)
