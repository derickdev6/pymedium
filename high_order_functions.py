from functools import reduce


def main():
    dofilter()
    domap()
    doreduce()


def doreduce():
    numbers = [2, 3, 4, 5]
    print('Numbers:', numbers)
    allmult = 1
    for i in numbers:
        allmult = allmult * i
    print('For cycle', allmult)
    allmulthof = reduce(lambda a, b: a * b, numbers)
    print('Reduce HOF:', allmulthof)


def domap():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Numbers:', numbers)
    elevate = [i**2 for i in numbers]
    print('List comprehension', elevate)
    elevatehof = list(map(lambda x: x**2, numbers))
    print('Map HOF:', elevatehof)


def dofilter():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Numbers:', numbers)
    odd = [i for i in numbers if i % 2 != 0]
    print('Lists comprehensions:', odd)

    oddhof = list(filter(lambda x: x % 2 != 0, numbers))
    print('Filter HOF:', oddhof)


if __name__ == '__main__':
    main()
