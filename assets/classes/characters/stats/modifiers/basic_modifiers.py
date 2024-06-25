# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
import math


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.stats.characteristics.basic_characteristics import BasicCharacteristics


# ##################################################
# КЛАССЫ
# ##################################################

class BasicModifiers:
    """
    Notes:
        Класс отвечает за модификаторы характеристик персонажа.

    Attributes:
        * self._strength (int): модификатор Силы персонажа;
        * self._dexterity (int): модификатор Ловкости персонажа;
        * self._endurance (int): модификатор Телосложения персонажа;
        * self._intelligence (int): модификатор Интеллекта персонажа;
        * self._wisdom (int): модификатор Мудрости персонажа;
        * self._charisma (int): модификатор Харизмы персонажа.

    Properties:
        * strength - геттер, отвечающий за получение значения модификатора Силы;
        * dexterity - геттер, отвечающий за получение значения модификатора Ловкости;
        * endurance - геттер, отвечающий за получение значения модификатора Телосложения;
        * intelligence - геттер, отвечающий за получение значения модификатора Интеллекта;
        * wisdom - геттер, отвечающий за получение значения модификатора Мудрости;
        * charisma - геттер, отвечающий за получение значения модификатора Харизмы.

    Raises:
        * TypeError: некорректный тип данных;
        * ValueError: некорректное значение.

    Methods:
        * calc_modifier - метод рассчитывает знчение модификатора.
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
            class_characteristics: BasicCharacteristics
    ) -> None:

        Check.value_type(
            value=class_characteristics,
            expected_type=BasicCharacteristics
        )

        self._class_characteristics: BasicCharacteristics = class_characteristics
        self._strength: int = self.calc_modifier(characteristic="strength")
        self._dexterity: int = self.calc_modifier(characteristic="dexterity")
        self._endurance: int = self.calc_modifier(characteristic="endurance")
        self._intelligence: int = self.calc_modifier(characteristic="intelligence")
        self._wisdom: int = self.calc_modifier(characteristic="wisdom")
        self._charisma: int = self.calc_modifier(characteristic="charisma")

    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def strength(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения модификатора Силы.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            (int): значение модификатора Силы.
        """

        Check.value_type(value=self._strength, expected_type=int)
        return self._strength

    @property
    def dexterity(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения модификатора Ловкости.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            (int): значение модификатора Ловкости.
        """

        Check.value_type(value=self._dexterity, expected_type=int)
        return self._dexterity

    @property
    def endurance(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения модификатора Телосложения.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            (int): значение модификатора Телосложения.
        """

        Check.value_type(value=self._endurance, expected_type=int)
        return self._endurance

    @property
    def intelligence(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения модификатора Интеллекта.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            (int): значение модификатора Интеллекта.
        """

        Check.value_type(value=self._intelligence, expected_type=int)
        return self._intelligence

    @property
    def wisdom(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения модификатора Мудрости.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            (int): значение модификатора Мудрости.
        """

        Check.value_type(value=self._wisdom, expected_type=int)
        return self._wisdom

    @property
    def charisma(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения модификатора Харизмы.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            (int): значение модификатора Харизмы.
        """

        Check.value_type(value=self._charisma, expected_type=int)
        return self._charisma


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def calc_modifier(
            self,
            characteristic: str
    ) -> int:
        """
        Notes:
            Метод рассчитывает модификатор по формуле:
            math.floor((characteristic - 10) / 2).

        Args:
            characteristic (int): значение характеристики для расчёта модификатора.

        Raises:
            ValueError: некорректное значение.

        Returns:
            int: значение модификатора.
        """

        Check.value_is_available(
            value=characteristic,
            available_values=BasicCharacteristics.get_available_characteristics()
        )

        match characteristic:
            case "strength":
                return math.floor((self._class_characteristics.strength - 10) / 2)

            case "dexterity":
                return math.floor((self._class_characteristics.dexterity - 10) / 2)

            case "endurance":
                return math.floor((self._class_characteristics.endurance - 10) / 2)

            case "intelligence":
                return math.floor((self._class_characteristics.intelligence - 10) / 2)

            case "wisdom":
                return math.floor((self._class_characteristics.wisdom - 10) / 2)

            case "charisma":
                return math.floor((self._class_characteristics.charisma - 10) / 2)

            case _:
                raise ValueError("Некорректное значение")
