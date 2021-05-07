import random


def main():
    print('Palindrome', palindrome(input('Word: ')))
    print('Divisors', divisors(input('Num: ')))


def palindrome(word):
    word = word.lower().replace(' ', '')
    assert len(
        word) > 1, 'Word must not be null or one char | White spaces count as 0'
    return word == word[::-1]


def divisors(num):
    assert num.isnumeric() and int(num) > 0, 'Only numbers > 0  allowed'
    num = int(num)
    return [i for i in range(1, num) if num % i == 0]


if __name__ == '__main__':
    main()
