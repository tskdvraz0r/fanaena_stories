# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
import math


# Сторонние библиотеки
...


# Проектные библиотеки
from classes.character.characteristics import Characteristics


# ##################################################
# КЛАССЫ
# ##################################################

class Modifiers:
    """
    Notes:
        ...

    Attributes:
        ...

    Properties:
        ...

    Raises:
        ...

    Methods:
        ...
    """

    # ##################################################
    # 1. АТРИБУТЫ КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 2. СВОЙСТВА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 3. МЕТОДЫ КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 4. ИНИЦИАЛИЗАЦИЯ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def __init__(
            self,
            class_characteristics: Characteristics
    ) -> None:
        """
        Notes:
            Инициализация экземпляра класса Модификаторов характеристик персонажа

        Args:
            class_characteristics (Characteristics): экземпляр класса Характеристик персонажа.
        """
        self._class_characteristics = class_characteristics
        self._strength: int = self.calc_modifier(self._class_characteristics.strength)
        self._dexterity: int = self.calc_modifier(self._class_characteristics.dexterity)
        self._endurance: int = self.calc_modifier(self._class_characteristics.endurance)
        self._intelligence: int = self.calc_modifier(self._class_characteristics.intelligence)
        self._wisdom: int = self.calc_modifier(self._class_characteristics.wisdom)
        self._charisma: int = self.calc_modifier(self._class_characteristics.charisma)


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def strength(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя Силы.
        """

        return self._strength

    @property
    def dexterity(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя Ловкости.
        """

        return self._dexterity

    @property
    def endurance(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя Телосложения.
        """

        return self._endurance

    @property
    def intelligence(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя Интеллекта.
        """

        return self._intelligence

    @property
    def wisdom(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя Мудрости.
        """

        return self._wisdom

    @property
    def charisma(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя Харизмы.
        """

        return self._charisma


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def calc_modifier(
            self,
            characteristic: int
    ) -> int:
        """
        Notes:
            Метод рассчитывает модификатор по формуле:
            math.floor((characteristic - 10) / 2).

        Args:
            characteristic (int): значение характеристики для расчёта модификатора.

        Returns:
            int: значение модификатора.
        """

        return math.floor((characteristic - 10) / 2)
