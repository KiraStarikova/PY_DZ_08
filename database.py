def add_database():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    post = input('Введите должность: ')
    salary = input('Введите заработную плату: ')
    directory = surname + ' ' + name + ' ' + phone + ' ' + post + ' ' + salary
    return directory

def find_database():
    return search_database(input('Введите данные поиска: '))

def changed_database(str):
    strList = str.split()
    print('Что нужно изменить? ')
    print('1. Фамилию\n2. Имя\n3. Номер телефона\n4. Должность\n5. Заработную плату')
    mode = input()
    newData = input('Новое значение => ')
    if mode == '1':
        strList[0] = newData
    elif mode == '2':
        strList[1] = newData
    elif mode == '3':
        strList[2] = newData
    elif mode == '4':
        strList[3] = newData
    elif mode == '5':
        strList[4] = newData
    return " ".join(strList)

def search_database(a):
    with open('database.txt', 'r', encoding='utf-8') as f:
        return [i.strip() for i in f.readlines() if a in i]

def changes_database():
    mass = search_database('')
    findC = find_database()
    while findC == []:
        print('Ничего не найдено')
        findC = find_database()
    if len(findC) > 1:
        print('Найденно несколько значений: ')
        for i in findC: print(i)
        findC = [findC[int(input('Введите номер нужного => ')) - 1]]
    for i in range(len(mass)):
        if mass[i] == findC[0]:
            mass[i] = changed_database(findC[0])
    return mass
