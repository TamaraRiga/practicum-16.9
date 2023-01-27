# Задание 16.9.1, 16.9.2
class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.width}, {self.height}.'

    def get_area(self):
        return self.width * self.height

rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1)  # Rectangle : 5, 10, 50, 100.
print('Area: ', rect_1.get_area())   # Area:  5000


# Задание 16.9.3
class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'''  # внимание на кавычки
client_1 = Clients('Иван', 'Петров', 'Москва', 50)
print(client_1)
# "Иван Петров. Москва. Баланс: 50 руб."


# Задание 16.9.4
class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'''

    def get_guest(self):
        return f'{self.name} {self.surname}, г.{self.city}.'

client_1 = Clients('Иван', 'Петров', 'Москва', 50)
client_2 = Clients('Мария', 'Ивановна', 'Сочи', 45)
client_3 = Clients('Олеся','Янина','Новосибирск',50)

guest_list = [client_1, client_2, client_3]

for guest in guest_list:
    print(guest.get_guest())
# Иван Петров, г.Москва.
# Мария Ивановна, г.Сочи.
# Олеся Янина, г.Новосибирск.