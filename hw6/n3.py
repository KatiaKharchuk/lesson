class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(selfself):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

manager = Position("Andre", 'Sir', "HR", 400000, 34660)
print(manager.get_full_name())
print(manager.position())
print(manager.get_full_profit())
