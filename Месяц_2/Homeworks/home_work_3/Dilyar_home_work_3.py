class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"CPU + Memory = {self.__cpu + self.__memory}"

    def __str__(self):
        return f"CPU: {self.__cpu} " \
               f"Memory: {self.__memory}"

    def __gt__(self, other):
        return self.memory > other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(f"Идет звонок на номер {sim} с сим-карты-{sim}")

    def __str__(self):
        return f"sim cards list: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, *sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Локация отмечена, ведется маршрут в {location}")

    def __str__(self):
        return f"CPU: {self.cpu} " \
               f"Memory:{self.memory} " \
               f"Sim card: {self.sim_cards_list}"

sim = ["1 - O!", "2 - Beeline"]
pc = Computer(3500, 8)
pcInfo = Computer.make_computations(pc)
tel = Phone(1)
smartP = SmartPhone(888, 6, sim[0])
smartP2 = SmartPhone(2500, 4, sim[1])
smartP.call("+996 500 12 34 56", sim[0])
smartP.use_gps("Аламедин")


print(pc)
print(tel)
print(pcInfo)
print(smartP)
print(smartP2)
print(pc > smartP)