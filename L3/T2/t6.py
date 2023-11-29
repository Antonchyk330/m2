'''
Напишіть калькулятор: програма отримує два числа 
і операцію, здійснює операцію і друкує результат.
Програма виконує такі операції: 
"+" - додавання, 
"-" - відняти від першого числа друге, 
"*" - помножити, 
"/" - розділити перше число на друге. 
Якщо введена якась інша операція, 
потрібно надрукувати рядок, який вказаний у змінній 
err1: "Помилка: невідома операція.
"Якщо введена операція ділення, і друге число дорівнює нулю, 
потрібно надрукувати рядок err2: "Помилка: ділити на нуль не можна."

'''
num1 = int(input("Введіть число 1:"))
num2 = int(input("Введіть число 2:"))
operation = input("Введіть операцію(+-/*):")
err1 = "Помилка: невідома операція."
err2 = "Помилка: ділити на нуль не можна."

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    if num2 == 0:
        print(err2)
    else:
        print(num1/num2)
else:
    print(err1)
