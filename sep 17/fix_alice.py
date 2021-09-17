def main():
    with open('alice.txt', 'r', encoding='utf-8') as in_file:
        with open('alice_fixed.txt', 'w', encoding='utf-8') as out_file:

            write = False
            for line in in_file:
                if write:
                    if not line.startswith('*** '):
                        out_file.write(line)

                if line.startswith('*** '):
                    if not write:
                        write = True
                    else:
                        break


if __name__ == '__main__':
    main()
