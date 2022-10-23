from database import *
from logger import *

print('Выберите, что нужно сделать с данными сотрудников: ')
print('1. Внести новые  данные\n\
2. Поиск данных сотрудника\n\
3. Вывести всех сотрудников на экран\n\
4. Внести изменения')
mode = input()
if mode == '1':
    write_database(add_database())

elif mode == '2':
    for i in find_database(): print(i)

elif mode == '3':
    for i in search_database(''): print(i)

elif mode == '4':
    write_re(changes_database())

else:
    print('Введено неверное значение!')
