# 2.1 Повторяем основные конструкции
""""""

"""
На easy
"""
a, b = int(input()), int(input())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** 0.5)

"""
Индекс массы тела
"""
m, h = float(input()), float(input())
imb = m / h ** 2
if imb < 18.5:
    rez = "Недостаточная масса"
elif 18.5 <= imb <= 25:
    rez = "Оптимальная масса"
else:
    rez = "Избыточная масса"
print(rez)

