'''
Програма радить, що робити далі. 
Вона може надрукувати один з трьох рядків - "Вчитися!", "Грати!", "Гуляти!", 
Запитуючи, чи зроблені уроки і гарна погода.


Напишіть програму: спочатку задається питання, чи зроблені уроки. 
Якщо відповідь "так", то програма запитує, чи гарна погода. 
Якщо на питання про уроки ми отримали відповідь "ні", потрібно надрукувати "Вчитися!". 
Якщо на питання про хорошу погоду отримана відповідь "так", програма друкує "Гуляти!",
Інакше (значить, погода погана) - друкує "Грати!".
'''
q1 = input("зроблені уроки?").lower()

if q1 == "ні":
    print("Вчитися!")
elif q1 == "так":
    q2 = input("гарна погодa?").lower()
    if q2 == "так":
        print("Гуляти!")
    elif q2 == "ні":
        print("Грати!")
    else:
        print("введіть так або ні")
else:
    print("введіть так або ні")
