# 3. Округление
# Дано: число с плавающей точкой.

#Задание: написать программу, которая будет округлять заданное число:

#2х знаков после запятой;
#до целого;
#дополнять слева столько нулей, сколько не хватает числу до 11 знаков.

print ('Введите число:')
num = input()
num = float(num)
print('x =','{0:.2f}'.format(num),'\n',round(num),'\n','{0:=012}'.format(num))
# в последнем выводе указано 12 потому что точка тоже считается за знак
# в моем понимании, "до 11 знаков" = "до 11 цифр", что не совпадает с примером, поэтому написала так