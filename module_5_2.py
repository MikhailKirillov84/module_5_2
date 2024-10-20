
class House:  # созданный класс(Hause)
    def __init__ (self, name, number_of_floors):  # метод(__init__) это конструктор, в нем создаются основные атрибуты

        self.name = name  # атрибут1 - название дома(Hause)
        self.number_of_floors = number_of_floors   # атрибут2 - количество этажей дома

    def go_to (self, new_floor):   # метод(goto) это переход(лифт) от 1 этажа до указанного значения(new_floor)
        self.new_floor = new_floor    # атрибут принимаемый значение при вызове функции(go_to)

        if new_floor >= self.number_of_floors or new_floor <= 1:   # условие1 внутри метода(go_to) сравнивает атрибуты из разных методов
            print("Такого этажа не существует")    # надпись если условие выполняется

        else:   # условие2 при котором перебирается принятое значение с первого элемента и выводится на печать, последовательно
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):  # метод(__len__) возвращает количество символов в строке, всегда целое число
        return self.number_of_floors  # возвращает количество этаже

    def __str__(self):  # метод(__str__) возвращает строковое представление
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"  # возвращает строку

# для модуля 5.1
# h1 = House('ЖК Горский', 18)  # добавление переменной1 в класс(Hause), с присвоением двух значений
# h2 = House('Домик в деревне', 2)   # добавление переменной2 в класс(Hause)
# print(h1.name, h1.number_of_floors)   #вызов переменной класса с атрибутами метода(__init__)
# print(h2.name, h2.number_of_floors)
# h1.go_to(5)   # вызов метода(go_to) с присвоением значения(на како этаж надо)
# h2.go_to(10)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(str(h1))
print(str(h2))

# __len__
print(len(h1))
print(len(h2))
