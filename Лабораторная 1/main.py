class Teapot:
    def __init__(self, capacity_volume: float, occupied_volume: float, temperature: bool):
        """
                Создание и подготовка к работе объекта "Стакан"
                :param capacity_volume: Объем стакана
                :param occupied_volume: Объем занимаемой жидкости
                :param temperature: Температура чайника
                Примеры:
                >>> teapot = Teapot(500,0,87)  # инициализация экземпляра класса
                """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем стакана должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем стакана должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

        if not isinstance(temperature, (int, float)):
            raise ValueError("Температура должна быть int или float")
        if temperature >= 1300:
            raise ValueError("Температура должна быть меньше температуры плавления чайника")
        self.boiling = temperature

        def is_empty_teapot(self) -> bool:
            """
            Функция которая проверяет является ли чайник пустым
            :return: Является ли чайник пустым
            Примеры:
            >>> teapot = Teapot(500,0,67)
            >>> teapot.is_empty_teapot()
            """
            ...

        def add_water_to_teapot(self, water: float) -> None:
            """
            Добавление воды в чайник.
            :param water: Объем добавляемой жидкости
            :raise ValueError: Если количество добавляемой жидкости превышает свободное место в чайнике, то вызываем ошибку
            Примеры:
            >>> teapot = Teapot(500,0,58)
            >>> teapot.add_water_to_teapot(200)
            """
            if not isinstance(water, (int, float)):
                raise TypeError("Добавляемая жидкость должна быть типа int или float")
            if water < 0:
                raise ValueError("Добавляемая жидкость должна положительным числом")
            ...

        def boiling(self) -> bool:
            """
            Кипение чайника.
            :return: Кипит ли чайник
            Примеры:
            >>> teapot = Teapot(500,0,119)
            >>> teapot.boiling()
            """

class Door:
    def __init__(self, material: str, closed: bool):
        """
        Создание и подготовка к работе объекта "Дверь"
        :param material: Материал двери
        :param closed: Закрыта ли дверь
        Примеры:
        >>> door = Door("Wood", False)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material

        if not isinstance(closed, bool):
            raise TypeError("Закрыта дверь или нет должен быть типа bool")

    def close(self) -> None:
        """
        Функция которая закрывает дверь
        Примеры:
        >>> door = Door("Wood", False)
        >>> door.close()
        """
        ...

    def open(self) -> None:
        """
        Функция которая открывает дверь
        Примеры:
        >>> door = Door("Wood", True)
        >>> door.open()
        """
        ...


class Sofa:
    def __init__(self, material: str, folded: bool, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Диван"
        :param material: Материал дивана
        :param folded: Разложен ли диван
        Примеры:
        >>> sofa = Sofa("Velour", False, 2)  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть типа str")
        self.material = material

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Объем дивана должен быть int или float")
        if occupied_volume < 0:
            raise ValueError("Диван не может не занимать места")
        self.occupied_volume = occupied_volume

        if not isinstance(folded, bool):
            raise TypeError("Сложен ли диван или нет должен быть типа bool")

    def fold(self) -> None:
        """
        Функция которая раскладывает диван
        Примеры:
        >>> sofa = Sofa("Velour", False, 2)
        >>> sofa.fold()
        """
        ...

    def saw_of(self, volume) -> None:
        """
        Функция которая распилит диван
        :param volume: Какой объем отпилят
        Примеры:
        >>> sofa = Sofa("Velour", False, 2)
        >>> sofa.saw_of(1)
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем должен быть типа int или float")
        if volume < 0:
            raise ValueError("Отпиливаемый объем должен положительным числом")
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
