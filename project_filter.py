def main():
    data = [
        {
            'name': 'Facundo',
            'age': 72,
            'organization': 'Platzi',
            'position': 'Technical Coach',
            'language': 'python',
        },
        {
            'name': 'Luisana',
            'age': 33,
            'organization': 'Globant',
            'position': 'UX Designer',
            'language': 'javascript',
        },
        {
            'name': 'Héctor',
            'age': 19,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'ruby',
        },
        {
            'name': 'Gabriel',
            'age': 20,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'javascript',
        },
        {
            'name': 'Isabella',
            'age': 30,
            'organization': 'Platzi',
            'position': 'QA Manager',
            'language': 'java',
        },
        {
            'name': 'Karo',
            'age': 23,
            'organization': 'Everis',
            'position': 'Backend Developer',
            'language': 'python',
        },
        {
            'name': 'Ariel',
            'age': 32,
            'organization': 'Rappi',
            'position': 'Support',
            'language': '',
        },
        {
            'name': 'Juan',
            'age': 17,
            'organization': '',
            'position': 'Student',
            'language': 'go',
        },
        {
            'name': 'Pablo',
            'age': 32,
            'organization': 'Master',
            'position': 'Human Resources Manager',
            'language': 'python',
        },
        {
            'name': 'Lorena',
            'age': 56,
            'organization': 'Python Organization',
            'position': 'Language Maker',
            'language': 'python',
        },
    ]
    print('\nAll\n')
    print('Size =', len(data))
    for i in data:
        print(i)

    only_h30 = list(filter(lambda x: x.get('age') > 30, data))
    print('\nOnly age > 30\n')
    print('Size =', len(only_h30))
    for i in only_h30:
        print(i)

    only_python = list(filter(lambda x: x.get('language') == 'python', data))
    print('\nOnly python\n')
    print('Size =', len(only_python))
    for i in only_python:
        print(i)

    only_platzi = list(
        filter(lambda x: x.get('organization') == 'Platzi', data))
    print('\nOnly platzi\n')
    print('Size =', len(only_platzi))
    for i in only_platzi:
        print(i)

    only_platzi_and_python = list(filter(lambda x: x.get(
        'organization') == 'Platzi' and x.get('language') == 'python', data))
    print('\nOnly Platzi python\n')
    print('Size =', len(only_platzi_and_python))
    for i in only_platzi_and_python:
        print(i)


if __name__ == '__main__':
    main()
