'''
Напишіть програму, яка три рази задає питання і 
три рази каже однакові фрази на відповіді «так» і «ні».
Приклади питань написані в програмі нагорі. 
Відповіді повинні бути або "Чудово! 
Ви талант!" (На відповідь "так") або 
"Ви можете навчитися, якщо захочете!"
'''

# Поставте три питання, наприклад:
# "Ви вмієте грати на піаніно?"
# "Ви вмієте грати в футбол?"
# "Ви вмієте кататися на скейті?"
# запам'ятовуйте відповіді в змінну:
# Answer = input ()

answer = input("Ви вмієте танцювати вальс?")
if answer == "так":
    print("Чудово! Ти талант!")
else:
    print("Ти можеш навчитися, якщо захочеш!")

answer = input("Ви вмієте плавати?")
if answer == "так":
    print("Чудово! Ти талант!")
else:
    print("Ти можеш навчитися, якщо захочеш!")

answer = input("Ви вмієте підскочити на 1 метр?")
if answer == "так":
    print("Чудово! Ти талант!")
else:
    print("Ти можеш навчитися, якщо захочеш!")
