'''
Змініть минулу програму так, щоб вона тривала до тих пір, 
поки не буде дана правильна відповідь. 
Для цього умова має бути не в умовному операторі, а в циклі while.
'''
answer = "білка"
guess = input("Тваринка, з шерсті якої стікає вода:").lower()
while guess != answer:
    print("Починається на Б")
    guess = input("Тваринка, з шерсті якої стікає вода:").lower()
print("Ви - науковець!")
