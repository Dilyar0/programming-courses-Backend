student = {
    "name": "Argen",
    "age": 20,
    "skills": ["english", "programming"],
    "bad habbits": "smoking"
}

student["gender"] = "male" #добавляет словарь
del student["bad habbits"] #удаляет элемент по ключ
deletet = student.pop() #удаляет и хранит себе значение

#==================================================================================================
car = dict(brand="BMW", model="e34", color="black")

car.update(year=1995) #добавляет словарь

#--------эти двое работают одинаково
car.get("model") # получаем эл.
car["model"] # получаем эл.
car2 = car.copy() #копирует 

for k, v in car.items():
    print(f'{k}: {v}')

#по отдельности выглядело бы так, а вместе этого можно использовать item()
print(car.keys())
print(car.values())
#==================================================================================================

student.update(car) #объединяет два словаря





