'''
Введіть два цілих числа a і b (при цьому a ≤ b). 
Виведіть в стовпчик всі числа від a до b включно.
'''
a = int(input("Введіть число a:"))
b = int(input("Введіть число b:"))
while a>b:
    print("Введіть числа, щоб а ≤ b!")
    a = int(input("Введіть число a:"))
    b = int(input("Введіть число b:"))

for i in range(a, b+1):
    print(i)
