number = int(input('Введите число: '))
print(number + 2)

age = int(input('Укажите ваш возраст: '))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Извините пользование данным ресурсом только с 18 лет")

number = int(input('Введите число: '))
while number < 0 or number > 10:
    number = int(input('Вы ввели неверное число.\n'
                       'Число должно быть от 0 до 10.\n'
                       'Попробуйте еще раз: '))
print(number**2)


var_1 = int(input('Введите число: '))
var_2 = int(input('Введите число: '))
var_3 = var_2
var_2 = var_1
print(var_3, var_2)


name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = int(input("Укажите ваш возраст: "))
weight = int(input("Укажите ваш вес: "))
if age < 30 and (weight >= 50 and weight <= 120):
    print('Здоров')
elif (age >= 30 and age < 40) and (weight <= 50 or weight >= 120):
    print('Пора заняться собой')
elif age >= 40 and (weight <= 50 or weight >= 120):
    print('Нужно  к врачу')
else:
    print('Здесь могла быть еще какая - о рекомендация')




















