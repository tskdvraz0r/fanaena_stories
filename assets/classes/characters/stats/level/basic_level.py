# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check


# ##################################################
# КЛАССЫ
# ##################################################

class BasicLevel:
    """
    Notes:
        Класс отвечает за уровни персонажа и опыт.

    Attributes:
        * _levels_and_expirience (dict[int, tuple[int, int]]) - словарь, где ключ - уровень, а в значении кортеж с необходимым количеством опыта для получения уровня и суммарного количества опыта персонажа, для получения уровня.

    Properties:
        * current_level - геттер, отвечающий за получение значения "Уровня" персонажа;
        * current_expirience - геттер, отвечающий за получение значения текущего количества опыта персонажа;
        * total_expirience - геттер, отвечающий за получение значения общего количества опыта персонажа;
        * needed_expirience_for_next_level - геттер, отвечающий за получение значения необходимого количества опыта персонажа для получения нового уровня;
        * needed_total_expirience_for_next_level - геттер, отвечающий за получение значения необходимого количества суммарного опыта персонажа для получения нового уровня;

    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * get_levels_and_expirience - Метод возвращает словарь с уровнями и необходимым количеством опыта для его получения;
    """

    # ##################################################
    # 1. АТРИБУТЫ КЛАССА
    # ##################################################
    _levels_and_expirience: dict[int, tuple[int, int]] = {
        1: (0, 0),
        2: (68, 68),
        3: (295, 363),
        4: (805, 1168),
        5: (1716, 2884),
        6: (3154, 6038),
        7: (5249, 11287),
        8: (8136, 19423),
        9: (11955, 31378),
        10: (16851, 48229)
    }


    # ##################################################
    # 2. СВОЙСТВА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 3. МЕТОДЫ КЛАССА
    # ##################################################
    @classmethod
    def get_levels_and_expirience(cls) -> dict[int, tuple[int, int]]:
        """
        Notes:
            Метод возвращает словарь с уровнями и необходимым количеством опыта для его получения.
            * Ключ - значение уровня;
            * Кортеж - количество опыта, необходимое для достижения уровня и суммарное количество опыта, полученное игроком, для достижения уровня.

        Returns:
            dict[int, tuple[int, int]]: Словарь с уровнями и необходимым количеством опыта для его получения.
        """

        return cls._levels_and_expirience


    # ##################################################
    # 4. ИНИЦИАЛИЗАЦИЯ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def __init__(
            self,
            start_level: int
    ) -> None:
        Check.value_type(
            value=start_level,
            expected_type=int
        )

        Check.value_is_available(
            value=start_level,
            available_values=range(
                1,
                1 + max(self._levels_and_expirience.keys())
            )
        )

        self._current_level: int = start_level
        self._current_expirience: int = 0
        self._total_expirience: int = self._levels_and_expirience[self._current_level][1]
        self._needed_expirience_for_next_level: int = self._levels_and_expirience[self._current_level + 1][0]
        self._needed_total_expirience_for_next_level: int = self._levels_and_expirience[self._current_level + 1][1]


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def current_level(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения "Уровня" персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение показателя "Уровня" персонажа.
        """

        Check.value_type(
            value=self._current_level,
            expected_type=int
        )

        return self._current_level

    @property
    def current_expirience(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества опыта персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение текущего количества опыта персонажа.
        """

        Check.value_type(
            value=self._current_expirience,
            expected_type=int
        )

        return self._current_expirience

    @property
    def total_expirience(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения общего количества опыта персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение общего количества опыта персонажа.
        """

        Check.value_type(
            value=self._total_expirience,
            expected_type=int
        )

        return self._total_expirience

    @property
    def needed_expirience_for_next_level(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения необходимого количества опыта персонажа для получения нового уровня.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение необходимого количества опыта персонажа для получения нового уровня.
        """

        Check.value_type(
            value=self._needed_expirience_for_next_level,
            expected_type=int
        )

        return self._needed_expirience_for_next_level

    @property
    def needed_total_expirience_for_next_level(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения необходимого количества суммарного опыта персонажа для получения нового уровня.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение необходимого количества суммарного опыта персонажа для получения нового уровня.
        """

        Check.value_type(
            value=self._needed_total_expirience_for_next_level,
            expected_type=int
        )

        return self._needed_total_expirience_for_next_level

    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
