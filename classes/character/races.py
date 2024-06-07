# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from classes.engine.data_validation.check import Check


# ##################################################
# КЛАССЫ
# ##################################################

class Race:
    """
    Notes:
        Класс, отвечающий за игровые расы.

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
    _available_races: dict[str, str] = {
        "Человек": "Human",
        "Ксилаат": "Xylaat",
        "Зенхаас": "Zenhaas",
        "Наара": "Naara"
    }


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
    def __init__(self) -> None:
        self._name: str = "Базовый класс игровой расы"
        self._strength: int = 0
        self._dexterity: int = 0
        self._endurance: int = 0
        self._intelligence: int = 0
        self._wisdom: int = 0
        self._charisma: int = 0


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def name(self) -> str:
        """
        Notes:
            Геттер, отвечающий за получение наименования расы.
        """

        Check.value_type(
            value=self._name,
            expected_type=str
        )

        return self._name


    @property
    def strength(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения расового модификатора Силы.
        """

        Check.value_type(
            value=self._strength,
            expected_type=int
        )

        return self._strength


    @property
    def dexterity(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения расового модификатора Ловкости.
        """

        Check.value_type(
            value=self._dexterity,
            expected_type=int
        )

        return self._dexterity


    @property
    def endurance(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения расового модификатора Телосложения.
        """

        Check.value_type(
            value=self._endurance,
            expected_type=int
        )

        return self._endurance


    @property
    def intelligence(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения расового модификатора Интеллекта.
        """

        Check.value_type(
            value=self._intelligence,
            expected_type=int
        )

        return self._intelligence


    @property
    def wisdom(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения расового модификатора Мудрости.
        """

        Check.value_type(
            value=self._wisdom,
            expected_type=int
        )

        return self._wisdom


    @property
    def charisma(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения расового модификатора Харизмы.
        """

        Check.value_type(
            value=self._charisma,
            expected_type=int
        )

        return self._charisma


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
