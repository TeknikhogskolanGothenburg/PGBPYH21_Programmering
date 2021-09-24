import pickle

def main():
    line = "Alice Alice beginning to get very tired of sitting by her sister on the"
    password = "jsiei8KJkhdsj8jhd8u388dscnvcx,.nzökndlisdfk,ndslkjdslkjflkji8ei383sda"
    encrypted = ""
    for i, c in enumerate(line):
        encrypted += chr(ord(c) ^ ord(password[i % len(password)]))
    print(encrypted)

    with open('encrypted.enc', 'wb') as crypto_file:
        pickle.dump(encrypted, crypto_file)


    with open('encrypted.enc', 'rb') as crypto_file:
        crypto = pickle.load(crypto_file)

    clear_text = ""
    for i, c in enumerate(crypto):
        clear_text += chr(ord(c) ^ ord(password[i % len(password)]))
    print(clear_text)


if __name__ == '__main__':
    main()
