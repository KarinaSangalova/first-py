first_name = input('Введите имя студента: ')
last_name = input('Введите фамилию студента: ')
try:
    year = int(input('Введите год рождения студента: '))
except ValueError:
    print('Это не число.')
    year = int(input('Введите год рождения студента: '))

print(first_name, last_name, year, sep='_')
first_name, last_name = last_name, first_name
print(first_name, last_name, year+60, sep='_')