def palindrome(word):
    try:
        if len(word) == 0:
            raise ValueError('No empty word allowed')
        return word == word[::-1]
    except ValueError as ve:
        print(ve)
        return False
    except TypeError as te:
        print('Only strings allowed')
        return False
    else:
        print('No errors were found')


def divisors(num):
    try:
        if num <= 0:
            raise ValueError('Only x > 0')
        divis = [i for i in range(1, num) if num % i == 0]
        return divis
    except ValueError as ve:
        print(ve)
        return []
    except TypeError:
        print('Type error only numbers > 0 accepted')
        return []
    except ZeroDivisionError:
        print("May not divide by zero")
        return []


def main():
    # print(palindrome('sanas'))
    print(divisors(int(input("X: "))))


if __name__ == '__main__':
    main()
