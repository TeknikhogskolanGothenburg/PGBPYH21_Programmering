key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
       'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
       'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
       'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
       'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
       'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
       'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}


def encipher(text):
    result = ""
    for c in text:
        # Only look up letters
        if c.isalpha():
            result += key[c] # hej hej
        else:  # Any other character will be stored as is
            result += c
    return result


def main():
    # Decoding the message
    print(encipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))

    # Creating a secret message
    print(encipher("This secret will be kept forever!"))


if __name__ == '__main__':
    main()