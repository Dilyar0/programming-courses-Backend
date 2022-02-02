# Классы
class Car:
    wheel_number=4
    
    def __init__(self, model, year, color, is_crashed, penalty_amount=0):
        self.model = model
        self.year = year
        self.color = color
        self.is_crashed = is_crashed
        self.penalty_amount = penalty_amount
        
    # методы
    def drive(self,city):
        print(f"Car {self.model} driving to {city}")
    
    def change_color(self, new_color):
        self.color = new_color

    def __str__(self,):
        return f"model {self.model}\n"  \
                f"year {self.year}\n" \
                f"color {self.color}\n" \
                f"is crashed {self.is_crashed}\n" \
                f"penalty anmount {self.penalty_amount} \n" \
                f"wheel number {self.wheel_number}"
                



mazda_car = Car(model="rx-8",year=2001,color="purple",is_crashed=True)
# print(mazda_car)

# Перезапись
mazda_car.color = "Green"
# вызов метода 
# change_color("white")

# ещё один класс
bmw_car = Car("BMW m5", 2019, "black", False, 500)
bmw_car.drive("Osh")
print(bmw_car)


