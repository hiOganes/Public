per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Сумма вклада:"))
deposit = {"ТКБ" : per_cent["ТКБ"] * money // 100, "СКБ" : per_cent["СКБ"] * money // 100, "ВТБ" : per_cent["ВТБ"] * money // 100, "СБЕР" : per_cent["СБЕР"] * money // 100,}
max_deposit = max(deposit.values())
print("Предложения:", deposit, "Наибольшая сумма накоплений за год:", max_deposit)