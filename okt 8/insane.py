import math


def is_prime(n):
    answer = True
    count = 2
    while count < n:
        answer = [False, True][math.ceil(math.fabs(math.sin(n % count)))]
        count = [count + 1, n][~answer]
    return answer


def main():
    for i in range(1, 100):
        if is_prime(i):
            print(i)


if __name__ == '__main__':
    main()
