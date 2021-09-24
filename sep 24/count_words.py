import re
from collections import defaultdict, Counter

def main():
    with open('alice_fixed.txt', 'r', encoding='utf--8') as in_file:
        content = in_file.read().lower()

    # split_on_space = content.split(' ')
    # split_on_whitespace = content.split()
    split_on_regex = re.split(r"[^a-zA-Z'’0-9-]+", content)


    """
    {
        'and': 35,
        'or': 28
    }
    ('and', 35)
    """
    count_dict = defaultdict(lambda: 0)
    for word in split_on_regex:
        count_dict[word] += 1

    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    for word, count in count_list[:100]:
        print(word, "=", count)

    print("-----")

    count_dict = {word: count for word, count in sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:100]}
    for word, count in count_dict.items():
        print(word, "=", count)

    longest = max(count_list, key=lambda x: len(x[0]))[0]
    print(longest)
    #top_100 = dict(sorted(search_in.items(), key=operator.itemgetter(1), reverse=True)[:100])


if __name__ == '__main__':
    main()
