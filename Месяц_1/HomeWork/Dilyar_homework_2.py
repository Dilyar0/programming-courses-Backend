while True:
    userInp = input('пишите слова: ("стоп" если хотите остановить) ')
    
    if userInp == "стоп":
        break
    string = userInp.lower()
    
    count = 0
    list1 = "ауоыиэяюёеaeiou"
    for i in string:
        if i in list1:
            count = count+1
            
    count2 = 0
    list2 = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
    for i in string:
        if i in list2:
            count2 = count2+1
            
    count3 = 0
    list3 = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁQWERTYUIOPASDFGHJKLZXCVBNM"
    for i in userInp:
        if i in list3:
            count3 = count3+1
            
    count4 = 0
    for i in userInp:
        if i in list1 or list2:
            count4 = count4+1
    
print(f"Слово: {userInp}")
print(f"Количество букв: {count4}")
print(f"Согласных букв: {count2}")
print(f"Гласных букв: {count}")
print(f"Прописные буквы: {count3}")
print(f'Гласные = {round(count2 / len(userInp) * 100,2)}%')
print(f'Согласные = {round(count3 / len(userInp) * 100, 2)}%')