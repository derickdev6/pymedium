def main():
    my_list = [1, 'Derick', True, 4.67]
    midict = {'firstname': 'Derick', 'lastname': 'Robinson'}

    super_list = [
        {'firstname': 'Derick', 'lastname': 'Robinson'},
        {'firstname': 'Patrick', 'lastname': 'Robinson'},
        {'firstname': 'Nathan', 'lastname': 'Robinson'}
    ]
    super_dict = {
        'natural': [1, 2, 3, 4, 5],
        'integer': [-1, -4, 0, 5],
        'float': [1.2, 5.6, 0.1]
    }

    for key, value in super_dict.items():
        print(key, ' - ', value)

    for i in range(len(super_list)):
        print(super_list[i])


if __name__ == '__main__':
    main()
