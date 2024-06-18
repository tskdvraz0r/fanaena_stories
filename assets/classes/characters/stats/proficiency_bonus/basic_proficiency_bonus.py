# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.stats.level.basic_level import BasicLevel


# ##################################################
# КЛАССЫ
# ##################################################

class BasicProficiencyBonus:
    """
    Notes:
        Класс отвечает за показатель "Бонуса Мастерства".

    Attributes:
        ...

    Properties:
        * proficiency_bonus - геттер, отвечающий за получение значения "Бонуса Мастрества".

    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * calc_proficiency_bonus - метод отвечает за расчёт бонуса мастерства, который зависит от уровня.
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
            class_level: BasicLevel
    ) -> None:
        Check.value_type(
            value=class_level,
            expected_type=BasicLevel
        )

        self._class_level: BasicLevel = class_level
        self._proficiency_bonus: int = self.calc_proficiency_bonus()


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def proficiency_bonus(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения "Бонуса Мастрества".

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение покащателя "Бонуса Мастерства".
        """

        Check.value_type(
            value=self._proficiency_bonus,
            expected_type=int
        )

        return self._proficiency_bonus


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def calc_proficiency_bonus(self) -> int:
        """
        Notes:
            Метод отвечает за расчёт бонуса мастерства, который зависит от уровня.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            int: значение бонуса мастерства.
        """

        Check.value_type(
            value=self._class_level.current_level,
            expected_type=int
        )

        return (self._class_level.current_level - 1) // 4 + 2
