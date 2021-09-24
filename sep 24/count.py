from collections import Counter
import re


def main():
    with open('alice_fixed.txt', 'r', encoding='utf--8') as in_file:
        content = in_file.read().lower()

    split_on_regex = re.split(r"[^a-zA-Z'’0-9-]+", content)

    word_counter = Counter(split_on_regex)
    for word, count in word_counter.most_common(100):
        print(word, '=', count)


if __name__ == '__main__':
    main()
