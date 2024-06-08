# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
...

# Проектные библиотеки
...

# ##################################################
# КЛАССЫ
# ##################################################

class Profession:
    """
    Notes:
        Класс отвечает за Профессии персонажа.

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
    _available_professions: dict[str, str] = {
        "Воин": "Warrior",
        "Следопыт": "Rouge",
        "Маг": "Wizzard"
    }


    # ##################################################
    # 2. СВОЙСТВА КЛАССА
    # ##################################################


    # ##################################################
    # 3. МЕТОДЫ КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 4. ИНИЦИАЛИЗАЦИЯ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def __init__(self) -> None:
        self._name: str = "Базовый класс Профессии"
        self._hp_dice: int = 6
        self._mp_dice: int = 6
        self._sp_dice: int = 6


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def name(self) -> str:
        """
        Notes:
            Геттер, отвечающий за получение наименования Профессии.

        Returns:
            str: наименование Профессии.
        """

        return self._name

    @property
    def hp_dice(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения кубика очков здоровья.

        Returns:
            str: значения кубика очков здоровья.
        """

        return self._hp_dice

    @property
    def mp_dice(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения кубика очков маны.

        Returns:
            str: значения кубика очков маны.
        """

        return self._mp_dice

    @property
    def sp_dice(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения кубика очков стамины.

        Returns:
            str: значения кубика очков стамины.
        """

        return self._sp_dice


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...