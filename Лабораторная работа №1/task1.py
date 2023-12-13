# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Cat:
    def __init__(self, name: str, sound: str, age: int):

        """
        Создание и подготовка к работе объекта "Кот"

        :param name: Имя кота
        :param sound: Звук, который издаёт кот
        :param age: Возраст кота

        :raise ValueError: возраст кота должен быть больше или равным 0

        Примеры:
        >>> cat = Cat("Vasya", "Meow", 10)
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(sound, str):
            raise TypeError("Голос кота должен иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен иметь тип int")
        if age <= 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.name = name
        self.sound = sound
        self.age = age

    def get_age(self) -> int:
        """
        Возврат возраста кота

        :return Возраст кота

        Примеры:
        >>> cat = Cat("Vasya", "Meow", 10)
        >>> cat.get_age()
        10
        """
        return self.age

    def guess_the_age(self, age: int) -> bool:
        """
        Попытка угадать возраст кота

        :param Возраст кота, который мы предполагаем

        :return Угадали ли возраст

        :raise TypeError: если возраст не типа str

        Примеры:
        >>> cat = Cat("Vasya", "Meow", 10)
        >>> cat.guess_the_age(9)
        False
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен иметь тип int")
        return self.age == age

    def rename(self, name: str):
        """
        Переименовывание кота

        :param Новое имя кота

        :raise TypeError: если тип имени не соответствует str

        Примеры:
        >>> cat = Cat("Vasya", "Meow", 10)
        >>> cat.rename("Vasya the Greatest")
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        self.name = name

class Dog:
    def __init__(self, name: str, food: str, age: int):
        """
        Создание и подготовка к работе объекта "Собака"

        :param name: Имя кота
        :param food: Еда, которую ест собака
        :param age: Возраст кота

        :raise ValueError: возраст собкаи должен быть больше или равным 0

        Примеры:
        >>> dog = Dog("Sharic", "Meat", 10)
        """

        if not isinstance(name, str):
            raise TypeError("Имя должно иметь тип str")
        if not isinstance(food, str):
            raise TypeError("Еда собаки должна иметь тип str")
        if not isinstance(age, int):
            raise TypeError("Возраст должен иметь тип int")
        if age <= 0:
            raise ValueError("Возраст не может быть отрицательным")

        self.name = name
        self.food = food
        self.age = age

    def reset_food(self, food: str):
        """
        Переименовывание собаки

        :param Новая еда собаки

        :raise TypeError: если тип еды не соответствует str

        Примеры:
        >>> dog = Dog("Sharic", "Meat", 10)
        >>> dog.reset_food("Vegetables fe")
        """
        if not isinstance(food, str):
            raise TypeError("Еда собаки должна иметь тип str")

        self.food = food

    def get_food(self) -> str:
        """
        Возврат еды собаки

        :return Еда собаки

        Примеры:
        >>> dog = Dog("Sharic", "Meat", 10)
        >>> dog.get_food()
        'Meat'
        """
        return self.food

    def guess_the_food(self, food: str) -> bool:
        """
        Попытка угадать любимую еду собаки

        :param Любимая еда собаки, которую, мы предполагаем, она любит

        :return Угадали ли еду

        :raise TypeError: если еда не типа str

        Примеры:
        >>> dog = Dog("Sharic", "Meat", 10)
        >>> dog.guess_the_food("Vegetables")
        False
        """
        if not isinstance(food, str):
            raise TypeError("Еда должна иметь тип str")
        return self.food == food

class Snake:
    def __init__(self, length: int, color: str, type: str):
        """
        Создание и подготовка к работе объекта "Змея"

        :param length: Длина змеи
        :param color: Окрас змеи
        :param type: тип змеи

        :raise ValueError: длина змеи не может быть меньше или равна 0

        Примеры:
        >>> snake = Snake(5, "orange", "yzh")
        """

        if not isinstance(type, str):
            raise TypeError("Тип змеи должен иметь тип str")
        if not isinstance(color, str):
            raise TypeError("Цвет змеи должен иметь тип str")
        if not isinstance(length, int):
            raise TypeError("Длина змеи должна иметь тип int")
        if length <= 0:
            raise ValueError("Длина змеи должна быть больше 0")

        self.length = length
        self.color = color
        self.type = type

    def increment_lenght(self) -> None:
        """
        Увеличивание длины змеи на 1 метр, она подросла

        Примеры:
        >>> snake = Snake(5, "orange", "yzh")
        >>> snake.increment_lenght()
        """

    def reset_type(self, new_type: str) -> None:
        """
        Изменение типа змеи, змея мутировала

        :param Новый тип змеи

        :raise TypeError: если новый тип змеи не типа str

        Примеры:
        >>> snake = Snake(5, "orange", "yzh")
        >>> snake.reset_type("Petnisty yzh")
        """

        if not isinstance(new_type, str):
            raise TypeError("Тип змеи должен иметь тип str")

        self.type = new_type

    def reset_color(self, new_color: str) -> None:
        """
        Изменение цвета змеи

        :param Новый цвет змеи

        :raise TypeError: если новый цвет змеи не типа str

        Примеры:
        >>> snake = Snake(5, "orange", "yzh")
        >>> snake.reset_color("green")
        """

        if not isinstance(new_color, str):
            raise TypeError("Цвет змеи должен иметь тип str")

        self.color = new_color



if __name__ == "__main__":
    cat = Cat("Vasya", "Meow", 10)# TODO работоспособность экземпляров класса проверить с помощью doctest
    dog = Dog("Sharic", "Meat", 5)
    snake = Snake(10, "orange", "yzh")
    doctest.testmod()
    pass
