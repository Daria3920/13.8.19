price_all = 0
while True:
    try:
        ticket_num = input('Количество билетов? ')
        ticket_num = int(ticket_num)
        if type(ticket_num) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_num):
    i += 1
    while True:
        try:
            age = input(f'Возраст №{i}?')
            age = int(age)
            if age < 18:
                print('Билет бесплатный')
            elif 25 > age >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_num >= 3:
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки при покупке от 3-х билетов')
else:
    price_all = price_all - ((price_all / 100) * 10)