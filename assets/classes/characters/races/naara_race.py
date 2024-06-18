# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
...

# Проектные библиотеки
from assets.classes.characters.races.basic_race import BasicRace

# ##################################################
# КЛАССЫ
# ##################################################

class NaaraRace(BasicRace):
    """
    Notes:
        Класс, отвечающий за игровую расу "Наара".

    Attributes:
        * self._name (str): наименование расы. По умолчанию "Наара";
        * self._strength (int): расовый модификатор Силы. По умолчанию 1;
        * self._dexterity (int): расовый модификатор Ловкости. По умолчанию 1;
        * self._endurance (int): расовый модификатор Телосложения. По умолчанию 1;
        * self._intelligence (int): расовый модификатор Интеллекта. По умолчанию 1;
        * self._wisdom (int): расовый модификатор Мудрости. По умолчанию 1;
        * self._charisma (int): расовый модификатор Харизмы. По умолчанию 1;

    Properties:
        * name - Геттер, отвечающий за получение наименования игровой расы;
        * strength - Геттер, отвечающий за получение значения расового модификатора Силы;
        * dexterity - Геттер, отвечающий за получение значения расового модификатора Ловкости;
        * intelligence - Геттер, отвечающий за получение значения расового модификатора Интеллекта;
        * wisdom - Геттер, отвечающий за получение значения расового модификатора Мудрости;
        * charisma - Геттер, отвечающий за получение значения расового модификатора Харизмы.

    Raises:
        * TypeError: некорректный тип данных.

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
    def __init__(self) -> None:
        super().__init__()

        self._name = "Наара"
        self._strength = 1
        self._dexterity = 1
        self._endurance = 1
        self._intelligence = 1
        self._wisdom = 1
        self._charisma = 1


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...