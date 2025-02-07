class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter the text")

    def printString(self):
        print(self.text.upper())

obj = StringManipulator() # Создаём объект класса
obj.getString() # Запрашиваем строку у пользователя
obj.printString() # Выводим её в верхнем регистре


        