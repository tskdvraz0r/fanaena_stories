# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
...

# Проектные библиотеки
from classes.engine.data_validation.check import Check
from classes.mechanics.basic.dice import Dice
from classes.character.modifiers import Modifiers
from classes.character.professions import Profession


# ##################################################
# КЛАССЫ
# ##################################################

class HMSP:
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
            class_profession: Profession,
            class_modifiers: Modifiers
    ) -> None:
        self._class_modifiers: Modifiers = class_modifiers
        self._class_profession: Profession = class_profession

        self._max_hp: int = 10 + self._class_modifiers.endurance
        self._max_mp: int = 10 + self._class_modifiers.intelligence
        self._max_sp: int = 10 + self._class_modifiers.dexterity

        self._hp: int = self._max_hp
        self._mp: int = self._max_mp
        self._sp: int = self._max_sp

    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def max_hp(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков жизни.

        Returns:
            (int): значение максимального количества очков жизни.
        """

        return self._max_hp

    @property
    def hp(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков жизни.

        Returns:
            (int): значение текущего количества очков жизни.
        """

        return self._hp

    @property
    def max_mp(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков маны.

        Returns:
            (int): значение максимального количества очков маны.
        """

        return self._max_mp

    @property
    def mp(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков маны.

        Returns:
            (int): значение текущего количества очков маны.
        """

        return self._mp

    @property
    def max_sp(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков стамины.

        Returns:
            (int): значение максимального количества очков стамины.
        """

        return self._max_sp

    @property
    def sp(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков стамины.

        Returns:
            (int): значение текущего количества очков стамины.
        """

        return self._sp

    @hp.setter
    def hp(
            self,
            new_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков жизни.

        Attributes:
            new_value (int): новое значение текущего количества очков жизней.
        """

        Check.value_type(
            value=new_value,
            expected_type=int
        )

        self._hp = min(new_value, self._max_hp)

    @mp.setter
    def mp(
            self,
            new_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков маны.

        Attributes:
            new_value (int): новое значение текущего количества очков маны.
        """

        Check.value_type(
            value=new_value,
            expected_type=int
        )

        self._mp = min(new_value, self._max_mp)

    @sp.setter
    def sp(
            self,
            new_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков стамины.

        Attributes:
            new_value (int): новое значение текущего количества очков стамины.
        """

        Check.value_type(
            value=new_value,
            expected_type=int
        )

        self._sp = min(new_value, self._max_sp)


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def update_max_hp(self) -> None:
        """
        Notes:
            Метод, отвечающий за установку нового значения максимального количества очков жизни.
        """

        self._max_hp += Dice(d=self._class_profession.hp_dice).roll() + self._class_modifiers.endurance


    def update_max_mp(self) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения максимального количества очков маны.
        """

        self._max_mp += Dice(d=self._class_profession.mp_dice).roll() + self._class_modifiers.intelligence


    def update_max_sp(self) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения максимального количества очков стамины.
        """

        self._max_sp += Dice(d=self._class_profession.sp_dice).roll() + self._class_modifiers.dexterity
