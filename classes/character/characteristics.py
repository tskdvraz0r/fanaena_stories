# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
...

# Проектные библиотеки
from classes.mechanics.basic.dice import Dice
from classes.character.races import Race

# ##################################################
# КЛАССЫ
# ##################################################

class Characteristics:
    """
    Notes:
        Класс отвечает за характеристики персонажа.

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
            class_race: Race
        ) -> None:
        """
        Notes:
            Инициализация экземпляра класса Характеристик персонажа.

        Args:
            claass_race
        """
        self._class_race: Race = class_race
        self._strength: int = self.gen_characteristic() + self._class_race.strength
        self._dexterity: int = self.gen_characteristic() + self._class_race.dexterity
        self._endurance: int = self.gen_characteristic() + self._class_race.endurance
        self._inteligence: int = self.gen_characteristic() + self._class_race.intelligence
        self._wisdom: int = self.gen_characteristic() + self._class_race.wisdom
        self._charisma: int = self.gen_characteristic() + self._class_race.charisma


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

        return self._inteligence

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
    def gen_characteristic(self) -> int:
        """
        Notes:
            Для генерации показателя характеристики, метод использует следующее
            правило DnD: бросается 4d6 и суммируются 3 наибольших значения.
        """

        roll_4d6: list[int, int, int, int] = [
            Dice(d=6).roll() for _ in range(4)
        ]

        return sum(sorted(roll_4d6)[1:])
