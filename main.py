def main():
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    numbers[0] = int(input())
    x = 0
    while True:
        temp = int(input())
        if (temp > numbers[x]):
            break
        x = x + 1
        numbers.append(temp)
    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
