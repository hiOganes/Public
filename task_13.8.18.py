# Для онлайн-конференции необходимо написать программу, 
# которая будет подсчитывать общую стоимость билетов. 
# Программа должна работать следующим образом:

# 1. В начале у пользователя запрашивается количество 
# билетов, которые он хочет приобрести на мероприятие.

# 2. Далее для каждого билета запрашивается возраст 
# посетителя, в соответствии со значением которого выбирается стоимость:

# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# 3. В результате программы выводится сумма к оплате. 
# При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно 
# получает 10% скидку на полную стоимость заказа.

# Для проверки загрузите полученное решение на GitHub и прикрепите ссылку.



tickets = int(input("При покупке от 4-х билетов действует скидка 10% от стоимости заказа!\n"
                   "Введите количество билетов, которое хотите приобрести на мероприятие: "))
age = list(map(int, input("Укажите через пробел возраст посетителей: ").split()))

while tickets != len(age):
    age = list(map(int, input("Количество посетителей не совпадает с количеством билетов.\n"
                              "Укажите через пробел возраст посетителей: ").split()))

price = []
for i in age:
    if i in range(0, 18):
        price.append(0)
    elif i in range(18, 25):
        price.append(990)
    else:
        price.append(1390)

if tickets > 3:
    print("Сумма к оплате с учетом скидки: ", sum(price) - ((sum(price) / 100) * 10), "рублей")
else:
    print("Сумма к оплате: ", sum(price), "рублей")
    
