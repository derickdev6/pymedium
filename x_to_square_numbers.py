def main(x):
    # Using cicle
    # squares = []
    # for i in x:
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # print(squares)

    # Using list comprehensions
    # squares = [i**2 for i in x if i % 3 == 0]
    # print(squares)

    challenge = [i for i in range(100000)
                 if i % 4 == 0
                 and i % 6 == 0
                 and i % 9 == 0]
    # Tambien se pudo haber buscado el MCM que es 36
    # hacer solo una comparacion
    print(challenge)


if __name__ == '__main__':
    main(range(1, 101))
