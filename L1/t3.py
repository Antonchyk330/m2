'''
Програма повинна обчислювати зріст користувача в папугах. 
Чому не виходить? 
Згадайте, навіщо потрібні функції int () і str ().
'''

r = input ("Який у тебе зріст (сантиметрів)?")
rost_p = 17
p = int(int(r) / rost_p)
answer = "Це " + str(p) + " папуг!"
print (answer)
