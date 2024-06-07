# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
import math


# Сторонние библиотеки
...


# Проектные библиотеки
from classes.engine.data_validation.check import Check


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
            strength: int,
            dexterity: int,
            endurance: int,
            intelligence: int,
            wisdom: int,
            charisma: int
    ) -> None:
        """
        Notes:
            Инициализация экземпляра класса Модификаторов характеристик персонажа

        Args:
            strength (int): показатель силы персонажа;
            dexterity (int): показатель ловкости персонажа;
            endurance (int): показатель выносливости персонажа;
            intelligence (int): показатель интеллекта персонажа;
            wisdom (int): показатель мудрости персонажа;
            charisma (int): показатель харизмы персонажа;
        """

        for value in (strength, dexterity, endurance,
                      intelligence, wisdom, charisma
        ):
            Check.value_type(
                value=value,
                expected_type=int
            )

        self._strength: int = self.calc_modifier(strength)
        self._dexterity: int = self.calc_modifier(dexterity)
        self._endurance: int = self.calc_modifier(endurance)
        self._intelligence: int = self.calc_modifier(intelligence)
        self._wisdom: int = self.calc_modifier(wisdom)
        self._charisma: int = self.calc_modifier(charisma)


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def strength(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя силы.
        """

        return self._strength

    @property
    def dexterity(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя ловкости.
        """

        return self._dexterity

    @property
    def endurance(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя выностивости.
        """

        return self._endurance

    @property
    def intelligence(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя интеллекта (эта характеристика
            бесполезна для вас!).
        """

        return self._inteligence

    @property
    def wisdom(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя мудрости.
        """

        return self._wisdom

    @property
    def charisma(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение показателя харизмы.
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
            ...

        Args:
            characteristic (int): значение характеристики для расчёта модификатора.

        Returns:
            int: значение модификатора.
        """

        return math.floor((characteristic - 10) / 2)
