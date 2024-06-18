# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.basic_race import BasicRace

from assets.classes.mechanics.dice.dice import Dice


# ##################################################
# КЛАССЫ
# ##################################################

class BasicCharacteristics:
    """
    Notes:
        Класс отвечает за характеристики персонажа.

    Attributes:
        * _available_characteristics (set[str]): множество наименований доступных характеристик персонажа;
        * self._strength (int): показатель Силы;
        * self._dexterity (int): показатель Ловкости;
        * self._endurance (int): показатель Телосложения;
        * self._intelligence (int): показатель Интеллекта;
        * self._wisdom (int): показатель Мудрости;
        * self._charisma (int): показатель Харизмы;

    Properties:
        * get_available_characteristics -
        * strength - геттер, отвечающий за получение значения характеристики Силы;
        * dexterity - геттер, отвечающий за получение значения характеристики Ловкости;
        * endurance - геттер, отвечающий за получение значения характеристики Телосложения;
        * intelligence - геттер, отвечающий за получение значения характеристики Интеллекта;
        * wisdom - геттер, отвечающий за получение значения характеристики Мудрости;
        * charisma - геттер, отвечающий за получение значения характеристики Харизмы

    Raises:
        * TypeError: некорректный тип данных;
        * ValueError: недоступное значение.

    Methods:
        * get_available_characteristics - метод класса, отвечающий за получение множества наименований доступных характеристик персонажа;
        * gen_characteristic_value - метод рассчитывает значение характеристики;
        * calc_characteristic - метод рассчитывает значение выбранной характеристики с учётом расового модификатора;
    """

    # ##################################################
    # 1. АТРИБУТЫ КЛАССА
    # ##################################################
    _available_characteristics: set[str] = {
        "strength",
        "dexterity",
        "endurance",
        "intelligence",
        "wisdom",
        "charisma"
    }


    # ##################################################
    # 2. СВОЙСТВА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 3. МЕТОДЫ КЛАССА
    # ##################################################
    @classmethod
    def get_available_characteristics(cls) -> set[str]:
        """
        Notes:
            Метод класса, отвечающий за получение множества наименований доступных характеристик персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            set[str]: множество наименований доступных характеристик персонажа.
        """

        return cls._available_characteristics


    # ##################################################
    # 4. ИНИЦИАЛИЗАЦИЯ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def __init__(
            self,
            class_race: BasicRace
    ) -> None:
        Check.value_type(value=class_race, expected_type=BasicRace)

        self._class_race: BasicRace = class_race
        self._strength: int = self.calc_characteristic(characteristic="strength")
        self._dexterity: int = self.calc_characteristic(characteristic="dexterity")
        self._endurance: int = self.calc_characteristic(characteristic="endurance")
        self._intelligence: int = self.calc_characteristic(characteristic="intelligence")
        self._wisdom: int = self.calc_characteristic(characteristic="wisdom")
        self._charisma: int = self.calc_characteristic(characteristic="charisma")


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def strength(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения характеристики Силы.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            (int): значение характеристики Силы.
        """

        Check.value_type(value=self._strength, expected_type=int)
        return self._strength

    @property
    def dexterity(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения характеристики Ловкости.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            (int): значение характеристики Ловкости.
        """

        Check.value_type(value=self._dexterity, expected_type=int)
        return self._dexterity

    @property
    def endurance(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения характеристики Телосложения.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            (int): значение характеристики Телосложения.
        """

        Check.value_type(value=self._endurance, expected_type=int)
        return self._endurance

    @property
    def intelligence(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения характеристики Интеллекта.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            (int): значение характеристики Интеллекта.
        """

        Check.value_type(value=self._intelligence, expected_type=int)
        return self._intelligence

    @property
    def wisdom(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения характеристики Мудрости.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            (int): значение характеристики Мудрости.
        """

        Check.value_type(value=self._wisdom, expected_type=int)
        return self._wisdom

    @property
    def charisma(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения характеристики Харизмы.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            (int): значение характеристики Харизмы.
        """

        Check.value_type(value=self._charisma, expected_type=int)
        return self._charisma


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def gen_characteristic_value(self) -> int:
        """
        Notes:
            Метод рассчитывает значение характеристики, используя следующее
            правило DnD: бросается 4d6 и суммируются 3 наибольших значения.

        Returns:
            (int): сумма трех максимальных значений, "выпавших" в результате броска 4d6.
        """

        roll_4d6: list[int] = [Dice(d=6).roll() for _ in range(4)]

        return sum(sorted(roll_4d6)[1:])

    def calc_characteristic(
            self,
            characteristic: str
    ) -> int:
        """
        Notes:
            Метод рассчитывает значение выбранной характеристики с учётом расового модификатора.

        Args:
            characteristic (str): наименование характеристики, для которой необходимо рассчитать значение.

        Raises:
            ValueError: недоступное значение.

        Returns:
            int: значение характеристики с учётом расового модификатора.
        """


        Check.value_is_available(
            value=characteristic,
            available_values=self._available_characteristics
        )

        gen_value: int = self.gen_characteristic_value()

        match characteristic:
            case "strength":
                return  gen_value + self._class_race.strength

            case "dexterity":
                return  gen_value + self._class_race.dexterity

            case "endurance":
                return  gen_value + self._class_race.endurance

            case "intelligence":
                return  gen_value + self._class_race.intelligence

            case "wisdom":
                return  gen_value + self._class_race.wisdom

            case "charisma":
                return  gen_value + self._class_race.charisma

            case _:
                raise ValueError("Недоступное значение")
