# 2. Python art
# Дано: маркер (символ) и толщина фигуры.

# Задание: написать программу, которая будет отображать заданную фигуру.

# Комментарий: не осилила сделать универсальную рисовалку (и не уверена, что это подразумевалось в задании),
# поэтому рисует только одну фигуру

print('Введите толщину фигуры:')
thick = input()
thick = int(thick)
f = 'P'

for i in range((thick+1)//2):
    print((f*thick*5).center(thick*6) + (' '* thick))

for i in range(thick+1):
    print((f*thick).center(thick*2) + (f*thick).center(thick*6))

for i in range((thick+1)//2):
    print((f*thick*5).center(thick*6))

for i in range(thick+1):
    print((f*thick).center(thick*2))

