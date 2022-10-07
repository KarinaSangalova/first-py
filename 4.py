try:
    years = int(input('Введите количество лет: '))
    exp = int(input('Введите количество экспонатов: '))
except:
    print('Это не число')
    years = int(input('Введите количество лет: '))
    exp = int(input('Введите количество экспонатов: '))
days = years*365+years//4
day_exp = 8*60/5
seen_exp = int(days*day_exp)
exp_seen = int(exp//day_exp//365)
exp_seen_days = int(exp//day_exp)
print('При заданном количестве лет будет просмотрено: ', seen_exp, "экспонатов")
print('При заданном количестве экспонатов будет потрачено количество лет: ', exp_seen)
print('При заданном количестве экспонатов будет потрачено кол-во дней: ', exp_seen_days)