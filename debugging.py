def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    num = int(input("Type a number: "))
    print(divisors(num))
    print("Finished")


if __name__ == '__main__':
    main()
