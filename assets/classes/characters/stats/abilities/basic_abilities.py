# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.stats.modifiers.basic_modifiers import BasicModifiers
from assets.classes.characters.stats.proficiency_bonus.basic_proficiency_bonus import BasicProficiencyBonus
from assets.classes.characters.stats.posessions.basic_posessions import BasicPosessions


# ##################################################
# КЛАССЫ
# ##################################################

class BasicAbilities:
    """
    Notes:
        Класс отвечает за способности персонажа.

    Attributes:
        # СИЛА
        * self._athletics (int): Атлетика - ;
        * self._capacity (int): Грузоподъемность - ;
        * self._pushing_and_carrying (int): Толкание/Волочение/Перенос- ;

        # ЛОВКОСТЬ
        * self._acrobatics (int): Акробатика - ;
        * self._stealth (int): Скрытность - ;
        * self._sleight_of_hand (int): Ловкость Рук - ;

        # ТЕЛОСЛОЖЕНИЕ
        * self._holding_breath (int): Задержка Дыхания - ;

        # ИНТЕЛЛЕКТ
        * self._analysis (int): Анализ - ;
        * self._history (int): История - ;
        * self._magic (int): Магия - ;
        * self._nature (int): Природа - ;
        * self._religion (int): Религия - ;

        # МУДРОСТЬ
        * self._animal_care (int): Уход за животными - ;
        * self._insight (int): Проницательность - ;
        * self._medicine (int): Медицина - ;
        * self._perception (int): Внимательность - ;
        * self._survival (int): Выживание - ;

        # ХАРИЗМА
        * self._deception (int): Обман - ;
        * self._intimidation (int): Запугивание - ;
        * self._performance (int): Выступление - ;
        * self._persuasion (int): Убеждение - ;

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
            class_modifiers: BasicModifiers,
            class_proficiency_bonus: BasicProficiencyBonus,
            class_posessions: BasicPosessions
    ) -> None:
        for value, expected_type in zip(
                (class_modifiers, class_proficiency_bonus, class_posessions),
                (BasicModifiers, BasicProficiencyBonus, BasicPosessions),
        ):
            Check.value_type(
                value=value,
                expected_type=expected_type
            )

        self._class_modifiers: BasicModifiers = class_modifiers
        self._class_proficiency_bonus: BasicProficiencyBonus = class_proficiency_bonus
        self._class_posessions: BasicPosessions = class_posessions

        # СИЛА
        self._athletics: int = self.calc_abilitie_value(abilitie="athletics")

        # ЛОВКОСТЬ
        self._acrobatics: int = self.calc_abilitie_value(abilitie="acrobatics")
        self._stealth: int = self.calc_abilitie_value(abilitie="stealth")
        self._sleight_of_hand: int = self.calc_abilitie_value(abilitie="sleight_of_hand")

        # ИНТЕЛЛЕКТ
        self._analysis: int = self.calc_abilitie_value(abilitie="analysis")
        self._history: int = self.calc_abilitie_value(abilitie="history")
        self._magic: int = self.calc_abilitie_value(abilitie="magic")
        self._nature: int = self.calc_abilitie_value(abilitie="nature")
        self._religion: int = self.calc_abilitie_value(abilitie="religion")

        # МУДРОСТЬ
        self._animal_care: int = self.calc_abilitie_value(abilitie="animal_care")
        self._insight: int = self.calc_abilitie_value(abilitie="insight")
        self._medicine: int = self.calc_abilitie_value(abilitie="medicine")
        self._perception: int = self.calc_abilitie_value(abilitie="perception")
        self._survival: int = self.calc_abilitie_value(abilitie="survival")

        # ХАРИЗМА
        self._deception: int = self.calc_abilitie_value(abilitie="deception")
        self._intimidation: int = self.calc_abilitie_value(abilitie="intimidation")
        self._performance: int = self.calc_abilitie_value(abilitie="performance")
        self._persuasion: int = self.calc_abilitie_value(abilitie="persuasion")



    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def athletics(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Атлетики.

        Returns:
            int: Значение навыка Атлетики.
        """

        Check.value_type(
            value=self._acrobatics,
            expected_type=int
        )

        return self._acrobatics

    @property
    def acrobatics(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Акробатика.

        Returns:
            int: Значение навыка Акробатика.
        """

        Check.value_type(
            value=self._acrobatics,
            expected_type=int
        )

        return self._acrobatics

    @property
    def stealth(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Скрытность.

        Returns:
            int: Значение навыка Скрытность.
        """

        Check.value_type(
            value=self._stealth,
            expected_type=int
        )

        return self._stealth

    @property
    def sleight_of_hand(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Ловкость Рук.

        Returns:
            int: Значение навыка Ловкость Рук.
        """

        Check.value_type(
            value=self._sleight_of_hand,
            expected_type=int
        )

        return self._sleight_of_hand

    @property
    def analysis(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Анализ.

        Returns:
            int: Значение навыка Анализ.
        """

        Check.value_type(
            value=self._analysis,
            expected_type=int
        )

        return self._analysis

    @property
    def history(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка История.

        Returns:
            int: Значение навыка История.
        """

        Check.value_type(
            value=self._history,
            expected_type=int
        )

        return self._history

    @property
    def magic(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Магия.

        Returns:
            int: Значение навыка Магия.
        """

        Check.value_type(
            value=self._magic,
            expected_type=int
        )

        return self._magic

    @property
    def nature(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Природа.

        Returns:
            int: Значение навыка Природа.
        """

        Check.value_type(
            value=self._nature,
            expected_type=int
        )

        return self._nature

    @property
    def religion(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Религия.

        Returns:
            int: Значение навыка Религия.
        """

        Check.value_type(
            value=self._religion,
            expected_type=int
        )

        return self._religion

    @property
    def animal_care(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Забота о Животных.

        Returns:
            int: Значение навыка Забота о Животных.
        """

        Check.value_type(
            value=self._animal_care,
            expected_type=int
        )

        return self._animal_care

    @property
    def insight(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Проницательность.

        Returns:
            int: Значение навыка Проницательность.
        """

        Check.value_type(
            value=self._insight,
            expected_type=int
        )

        return self._insight

    @property
    def medicine(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Медицина.

        Returns:
            int: Значение навыка Медицина.
        """

        Check.value_type(
            value=self._medicine,
            expected_type=int
        )

        return self._medicine

    @property
    def perception(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Восприятие.

        Returns:
            int: Значение навыка Восприятие.
        """

        Check.value_type(
            value=self._perception,
            expected_type=int
        )

        return self._perception

    @property
    def survival(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Выживание.

        Returns:
            int: Значение навыка Выживание.
        """

        Check.value_type(
            value=self._survival,
            expected_type=int
        )

        return self._survival

    @property
    def deception(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Обман.

        Returns:
            int: Значение навыка Обман.
        """

        Check.value_type(
            value=self._deception,
            expected_type=int
        )

        return self._deception

    @property
    def intimidation(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Запугивание.

        Returns:
            int: Значение навыка Запугивание.
        """

        Check.value_type(
            value=self._intimidation,
            expected_type=int
        )

        return self._intimidation

    @property
    def performance(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Выступление.

        Returns:
            int: Значение навыка Выступление.
        """

        Check.value_type(
            value=self._performance,
            expected_type=int
        )

        return self._performance

    @property
    def persuasion(self) -> int:
        """
        Notes:
            Геттер, отвечающий за получение значения навыка Убеждение.

        Returns:
            int: Значение навыка Убеждение.
        """

        Check.value_type(
            value=self._persuasion,
            expected_type=int
        )

        return self._persuasion


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def calc_abilitie_value(
            self,
            abilitie: str
    ) -> int:
        """
        Notes:
            Метод принимает на вход название способности и рассчитывает значение с учётом владения и бонуса мастерства.

        Args:
            abilitie (str): Название способности.

        Returns:
            int: Значение способности.
        """

        match abilitie:
            case abilitie if abilitie in {"athletics"}:
                return (
                    self._class_modifiers.strength
                    if self._class_posessions.abilities[abilitie] == False
                    else self._class_modifiers.strength
                    + self._class_proficiency_bonus.proficiency_bonus
                )

            case abilitie if abilitie in {
                "acrobatics",
                "stealth",
                "sleight_of_hand",
            }:
                return (
                    self._class_modifiers.dexterity
                    if self._class_posessions.abilities[abilitie] == False
                    else self._class_modifiers.dexterity
                    + self._class_proficiency_bonus.proficiency_bonus
                )

            case abilitie if abilitie in {
                "analysis",
                "history",
                "magic",
                "nature",
                "religion",
            }:
                return (
                    self._class_modifiers.intelligence
                    if self._class_posessions.abilities[abilitie] == False
                    else self._class_modifiers.intelligence
                    + self._class_proficiency_bonus.proficiency_bonus
                )

            case abilitie if abilitie in {
                "animal_care",
                "insight",
                "medicine",
                "perception",
                "survival",
            }:
                return (
                    self._class_modifiers.wisdom
                    if self._class_posessions.abilities[abilitie] == False
                    else self._class_modifiers.wisdom
                    + self._class_proficiency_bonus.proficiency_bonus
                )

            case abilitie if abilitie in {
                "deception",
                "intimidation",
                "performance",
                "persuasion",
            }:
                return (
                    self._class_modifiers.charisma
                    if self._class_posessions.abilities[abilitie] == False
                    else self._class_modifiers.charisma
                    + self._class_proficiency_bonus.proficiency_bonus
                )

            case _:
                return 0
