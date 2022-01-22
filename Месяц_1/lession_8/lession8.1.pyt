from datetime import datetime
from random import choice

 
students = [
    {2: "Эдиль"},
    {4: "Амантур"},
    {6: "Аман"},
    {7: "ырыскелди"},
    {10: "Атабек"},
    {11: "Исмет"},
    {12: "Дильяр"},
    {13: "Сыргабек"},
]

c = len(students)
while c != 0:
    random_student = student.index(choice(student))
    print(students.pop(random_student))
    command = input("Задайте вопрос: ")
    rate = input(f"Постовте оценку: {students[random_student]} ")

    for i in students:
        for k,v in i.items():
            print(f"{k}: {v}")