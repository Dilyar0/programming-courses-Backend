# инкапсуляция - нужно для того чтобы скрывать элементов, чтобы сделать некоторые элементы более безопасными
# чтобы 
class Animal:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    def speak(self):
        pass

    def _creat_animal(self):
        print("New animal is created")

    # this is Анотация
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 15:
            print("Wrong value for name it must be less than 15 corrects")
        else:
            self.__name = name
# у нас есть GET и SET. гет- получаем значение. сет- задаем
# только вот так мы можем получать приватные атрибуты
    def get_age(self):
        return self.__age
# изменение age с условием
    def set_age(self, new_age):
        if new_age <= 0:
            print("Wrong value for age, it must be positive number")
        else:
            self.__age = new_age

    def info(self):
        return f"Name: {self.__name}, Age: {self.__age}, Color: {self.__color}"

class Cat(Animal):
    def __init__(self, name, age, color,lifes):
        Animal.__init__(self, name, age, color)
        self.__lifes = lifes
        self._created_animal()
        
    def speak(self):
        print("Cat say meaw")

class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def speak(self):
        print("Dog say gav")
    

# присваивание значение к атрибутам
some_animal = Animal("Bobik",2, "Brown")

# попытаемся изменить значение 
some_animal.age = -5
print(some_animal.info())
# Так не получится так-как атрибут приватный

# вот так можно изменить, мы обезопасили себя(инкапсулировали), теперь пользователь не может вводит некоректные цифра
some_animal.set_age(9)
print(some_animal.info())


some_animal.name = "Barsik"
print(some_animal.name)

tom_cat = Cat("Tom", 3, "Blue", 9)
