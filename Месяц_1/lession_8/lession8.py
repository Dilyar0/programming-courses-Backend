import time
# open - это функция которая открывает, если нет то создает файл
# первым параметром он принимает название файла, 
# вторым параметром он принимает режим файла

# file = open("file.txt", "w")
# file.write("python first month")
# file.close()

# режим файлов
r = "режим чтение"
w = "режим записи"
a = "режим до записи"
x = "режим создание нового файла"

# новый вид создание файла
with open("hymn.txt", "a") as file:
    for i in file.read():
        print(i, end="")
        time.sleep(0,2)