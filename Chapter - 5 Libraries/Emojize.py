import emoji

def emojize(text):
    print(emoji.emojize("Output: " + text, language = 'alias'))

emojize(input("Input: "))