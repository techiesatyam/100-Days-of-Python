def main():
    word = input("Input: ")
    print("Output:", shorten(word))

def shorten(word):
    result = ""
    for letter in word:
        if letter not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            result += letter
    return result

if __name__ == "__main__":
    main()