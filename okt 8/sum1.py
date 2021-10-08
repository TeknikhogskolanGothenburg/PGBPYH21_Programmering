def main():
    # Sum all numbers between 10 and 1,000
    a = 10
    b = 1000
    total_sum = 0
    while b >= a:
        total_sum += a
        a += 1

    print(total_sum)


if __name__ == '__main__':
    main()
