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

class BasicPosessions:
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
    _abilities: dict[str, bool] = {
        # СИЛА
        "athletics": False,

        # ЛОВКОСТЬ
        "acrobatics": False,
        "stealth": False,
        "sleight_of_hand": False,

        # ИНТЕЛЛЕКТ
        "analysis": False,
        "history": False,
        "magic": False,
        "nature": False,
        "religion": False,

        # МУДРОСТЬ
        "animal_care": False,
        "insight": False,
        "medicine": False,
        "perception": False,
        "survival": False,

        # ХАРИЗМА
        "deception": False,
        "intimidation": False,
        "performance": False,
        "persuasion": False,
    }

    _armors: dict[str, bool] = {
        "shields": False,
        "light_armor": False,
        "medium_armor": False,
        "heavy_armor": False,
    }

    _tools: dict[str, bool] = {
        "thieves": False,
        "alchemists": False,
        "calligraphers": False,
        "cartographers": False,
    }

    _transports: dict[str, bool] = {
        "horse": False,
        "carriege": False,
        "boat": False,
        "ship": False,
    }

    _weapons: dict[str, bool] = {
        "staff": False,
        "spear": False,
        "dagger": False,
        "sword": False,
        "hammer": False,
        "axe": False,
        "mace": False,
        "bow": False,
        "crossbow": False,
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
        self._abilities: dict[str, bool] = BasicPosessions._abilities
        self._armors: dict[str, bool] = BasicPosessions._armors
        self._tools: dict[str, bool] = BasicPosessions._tools
        self._transport: dict[str, bool] = BasicPosessions._transports
        self._weapons: dict[str, bool] = BasicPosessions._weapons


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def abilities(self) -> dict[str, bool]:
        """
        Notes:
            Геттер, отвечающий за получение словаря с владениями навыками.

        Returns:
            dict[str, bool]: Словарь с владениями навыков.
        """

        return self._abilities


    @property
    def armors(self) -> dict[str, bool]:
        """
        Notes:
            Геттер, отвечающий за получение словаря с владениями бронёй.

        Returns:
            dict[str, bool]: Словарь с владениями навыков.
        """

        return self._armors


    @property
    def weapons(self) -> dict[str, bool]:
        """
        Notes:
            Геттер, отвечающий за получение словаря с владениями оружием.

        Returns:
            dict[str, bool]: Словарь с владениями навыков.
        """

        return self._weapons


    @property
    def tools(self) -> dict[str, bool]:
        """
        Notes:
            Геттер, отвечающий за получение словаря с владениями инструментами.

        Returns:
            dict[str, bool]: Словарь с владениями навыков.
        """

        return self._tools


    @property
    def transport(self) -> dict[str, bool]:
        """
        Notes:
            Геттер, отвечающий за получение словаря с владениями транспортом.

        Returns:
            dict[str, bool]: Словарь с владениями навыков.
        """

        return self._transport


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
