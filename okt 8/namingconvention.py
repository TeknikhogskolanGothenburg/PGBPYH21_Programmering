# Constant values are named using SCREAMING_SNAKE_CASE
RED = (255, 0, 0)
BLUE_COLOR = (0, 255, 0)


# Classes are named using CapWords
class BasketballTeam:
    def method1(self):
        pass

    def method2(self):
        pass


def snake_case_name(this_is_also_snake_case):
    for i in range(10):
        pass

    print("Something")


def main():
    # Variables and functions are named using snake_case
    final_score = 10  # Two spaces before line comment
    # camelCase -> finalScore
    print("We have a limit for how long a line can be and this line will eventually break this rule. The rule says that"
          " no line should exceed 79 characters")

    result = "ABC" "DEF"
    print(result)



if __name__ == '__main__':
    main()
