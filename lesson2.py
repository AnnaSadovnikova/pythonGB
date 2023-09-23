#Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


n = int(input())
count_orel = 0
count_reshka = 0

for i in range(n):
    side = int(input())
    if side == 1:
        count_reshka+=1

    else:
        count_orel+=1

print(min(count_orel, count_reshka))

#Мне выдает ошибку 
#ValueError: invalid literal for int() with base 10: '/usr/local/bin/python3 /Users/el.kuwaitmail.ru/Documents/GeekBrains/python/lesson2.py'
#el.kuwaitmail.ru@Annas-MacBook-Pro python % /usr/local/bin/python3 /Users/el.kuwaitmail.ru/Documents/GeekBrains/python/lesson2.py
#/usr/local/bin/python3 /Users/el.kuwaitmail.ru/Documents/GeekBrains/python/lesson2.py
#Traceback (most recent call last):
#  File "/Users/el.kuwaitmail.ru/Documents/GeekBrains/python/lesson2.py", line 8, in <module>
#    n = int(input())
#        ^^^^^^^^^^^^
#ValueError: invalid literal for int() with base 10: '/usr/local/bin/python3 /Users/el.kuwaitmail.ru/Documents/GeekBrains/python/lesson2.py'
#el.kuwaitmail.ru@Annas-MacBook-Pro python % 