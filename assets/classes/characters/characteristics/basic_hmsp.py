# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.mechanics.dice.dice import Dice

from assets.classes.characters.characteristics.basic_modifiers import BasicModifiers
from assets.classes.characters.professions.basic_profession import BasicProfession



# ##################################################
# КЛАССЫ
# ##################################################

class BasicHMSP:
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
            class_profession: BasicProfession,
            class_modifiers: BasicModifiers
    ) -> None:
        Check.value_type(
            value=class_profession,
            expected_type=BasicProfession
        )

        Check.value_type(
            value=class_modifiers,
            expected_type=BasicModifiers
        )

        self._class_profession: BasicProfession = class_profession
        self._class_modifiers: BasicModifiers = class_modifiers

        self._max_health_points: int = self._class_profession.health_points_dice + self._class_modifiers.endurance
        self._max_mind_points: int = self._class_profession.mind_points_dice + self._class_modifiers.intelligence
        self._max_mana_points: int = self._class_profession.mana_points_dice + self._class_modifiers.intelligence
        self._max_stamina_points: int = self._class_profession.stamina_points_dice + self._class_modifiers.endurance

        self._current_health_points: int = self._max_health_points
        self._current_mind_points: int = self._max_mind_points
        self._current_mana_points: int = self._max_mana_points
        self._current_stamina_points: int = self._max_stamina_points


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def max_health_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков телесного здоровья.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение максимального количества очков телесного здоровья.
        """

        Check.value_type(
            value=self._max_health_points,
            expected_type=int
        )
        return self._max_health_points

    @property
    def max_mind_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков ментального здоровья.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение максимального количества очков ментального здоровья.
        """

        Check.value_type(
            value=self._max_mind_points,
            expected_type=int
        )
        return self._max_mind_points

    @property
    def max_mana_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков маны.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение максимального количества очков маны.
        """

        Check.value_type(
            value=self._max_mana_points,
            expected_type=int
        )
        return self._max_mana_points

    @property
    def max_stamina_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения максимального количества очков стамины.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение максимального количества очков стамины.
        """

        Check.value_type(
            value=self._max_stamina_points,
            expected_type=int
        )
        return self._max_stamina_points

    @property
    def current_health_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков телесного здоровья.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение текущего количества очков телесного здоровья.
        """

        Check.value_type(
            value=self._current_health_points,
            expected_type=int
        )
        return self._current_health_points

    @property
    def current_mind_points(self) -> int: # type: ignore
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков ментального здоровья.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение текущего количества очков ментального здоровья.
        """

        Check.value_type(
            value=self._current_mind_points,
            expected_type=int
        )
        return self._current_mind_points

    @property
    def current_mana_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков маны.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение текущего количества очков маны.
        """

        Check.value_type(
            value=self._current_mana_points,
            expected_type=int
        )
        return self._current_mana_points

    @property
    def current_stamina_points(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения текущего количества очков стамины.

        Raises:
            TypeError: некорректный тип данных.

        Returns:
            int: значение текущего количества очков стамины.
        """

        Check.value_type(
            value=self._current_stamina_points,
            expected_type=int
        )
        return self._current_stamina_points

    @current_health_points.setter
    def current_health_points(
            self,
            new_health_points_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков телесного здоровья.

        Raises:
            TypeError: некорректный тип данных.
        """

        Check.value_type(
            value=new_health_points_value,
            expected_type=int
        )
        self._current_health_points = new_health_points_value

    @current_mind_points.setter
    def current_mind_points( # type: ignore
            self,
            new_mind_points_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков ментального здоровья.

        Raises:
            TypeError: некорректный тип данных.
        """

        Check.value_type(
            value=new_mind_points_value,
            expected_type=int
        )
        self._current_mind_points = new_mind_points_value

    @current_mana_points.setter
    def current_mind_points(
            self,
            new_mana_points_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков маны.

        Raises:
            TypeError: некорректный тип данных.
        """

        Check.value_type(
            value=new_mana_points_value,
            expected_type=int
        )
        self._current_mana_points = new_mana_points_value

    @current_stamina_points.setter
    def current_stamina_points(
            self,
            new_stamina_points_value: int
    ) -> None:
        """
        Notes:
            Сеттер, отвечающий за установку нового значения текущего количества очков стамины.

        Raises:
            TypeError: некорректный тип данных.
        """

        Check.value_type(
            value=new_stamina_points_value,
            expected_type=int
        )
        self._current_stamina_points = new_stamina_points_value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def update_max_health_points(self) -> None:
        """
        Notes:
            Метод, отвечающий за установку нового значения максимального количества очков телесного здоровья.
        """

        health_points_dice: Dice = Dice(d=self._class_profession.health_points_dice)
        self._max_health_points += health_points_dice.roll() + self._class_modifiers.endurance

    def update_max_mind_points(self) -> None:
        """
        Notes:
            Метод, отвечающий за установку нового значения максимального количества очков ментального здоровья.
        """

        mind_points_dice: Dice = Dice(d=self._class_profession.mind_points_dice)
        self._max_mind_points += mind_points_dice.roll() + self._class_modifiers.intelligence

    def update_max_mana_points(self) -> None:
        """
        Notes:
            Метод, отвечающий за установку нового значения максимального количества очков маны.
        """

        mana_points_dice: Dice = Dice(d=self._class_profession.mana_points_dice)
        self._max_mana_points += mana_points_dice.roll() + self._class_modifiers.intelligence

    def update_max_stamina_points(self) -> None:
        """
        Notes:
            Метод, отвечающий за установку нового значения максимального количества очков стамины.
        """

        stamina_points_dice: Dice = Dice(d=self._class_profession.stamina_points_dice)
        self._max_stamina_points += stamina_points_dice.roll() + self._class_modifiers.endurance
