# 1. Fizz Buzz
# Дано: Число, как целочисленное (int).
# Задание:
# "Fizz buzz" это игра со словами, с помощью которой мы будем учить наших роботов делению. Давайте обучим компьютер.

# Вы должны написать программу, которая принимает положительное целое число и возвращает сл. значения.
#
# "Fizz Buzz", если число делится на 3 и 5;
# "Fizz", если число делится на 3;
# "Buzz", если число делится на 5;

# это второй вариант решения, первый находится в файле "task1"

print ('Поиграем в Fizz Buzz! Будет весело (или нет, не мои проблемы) ')
print ('Введите число: ')
x = input()
res = ('Fizz Buzz' if (int(x)%3 == 0) & (int(x)%5 == 0) else
       'Fizz' if int(x)%3 == 0 else
       'Buzz' if int(x)%5 == 0 else
       x)
print (res);
