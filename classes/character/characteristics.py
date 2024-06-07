# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
...

# Проектные библиотеки
from classes.mechanics.basic.dice import Dice
from classes.engine.data_validation.check import Check

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
            race_strength: int,
            race_dexterity: int,
            race_endurance: int,
            race_intelligence: int,
            race_wisdom: int,
            race_charisma: int
        ) -> None:
        """
        Notes:
            Инициализация экземпляра класса Характеристик персонажа.

        Args:
            race_strength (int): расовый модификатор силы персонажа;
            race_dexterity (int): расовый модификатор ловкости персонажа;
            race_endurance (int): расовый модификатор выносливости персонажа;
            race_intelligence (int): расовый модификатор интеллекта персонажа;
            race_wisdom (int): расовый модификатор мудрости персонажа;
            race_charisma (int): расовый модификатор харизмы персонажа;
        """

        for value in (race_strength, race_dexterity, race_endurance,
                      race_intelligence, race_wisdom, race_charisma
        ):
            Check.value_type(
                value=value,
                expected_type=int
            )

        self._strength: int = self.gen_characteristic() + race_strength
        self._dexterity: int = self.gen_characteristic() + race_dexterity
        self._endurance: int = self.gen_characteristic() + race_endurance
        self._inteligence: int = self.gen_characteristic() + race_intelligence
        self._wisdom: int = self.gen_characteristic() + race_wisdom
        self._charisma: int = self.gen_characteristic() + race_charisma


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
