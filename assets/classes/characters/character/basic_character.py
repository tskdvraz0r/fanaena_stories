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
from assets.classes.characters.professions.basic_profession import BasicProfession
from assets.classes.characters.stats.characteristics.basic_characteristics import BasicCharacteristics
from assets.classes.characters.stats.modifiers.basic_modifiers import BasicModifiers
from assets.classes.characters.stats.hmsp.basic_hmsp import BasicHMSP
from assets.classes.characters.stats.level.basic_level import BasicLevel
from assets.classes.characters.stats.proficiency_bonus.basic_proficiency_bonus import BasicProficiencyBonus
from assets.classes.characters.stats.abilities.basic_abilities import BasicAbilities

from assets.classes.characters.stats.posessions.basic_abilities_posessions import BasicAbilitiesPosessions
from assets.classes.characters.stats.posessions.basic_armors_posessions import BasicArmorsPosessions
from assets.classes.characters.stats.posessions.basic_common_tools_posessions import BasicCommonToolsPossessions
from assets.classes.characters.stats.posessions.basic_craft_tools_posessions import BasicCraftToolsPosessions
from assets.classes.characters.stats.posessions.basic_transtort_posessions import BasicTransportPosessions
from assets.classes.characters.stats.posessions.basic_weapons_posessions import BasicWeaponsPosessions


# ##################################################
# КЛАССЫ
# ##################################################

class BasicCharacter:
    """
    Notes:
        Базовый класс, отвечающий за создание персонажей.

    Attributes:
        * self._name (str): имя персонажа;
        * self._surname (str): фамилия персонажа;
        * self._fullname (str): имя и фамилия персонажа;
        * self._class_race (BasicRace): экземпляр класса расы персонажа;
        * self._class_profession (BasicProfession): экземпляр класса профессии персонажа;
        * self._class_characteristics (BasicCharacteristics): экземпляр класса характеристик персонажа;
        * self._class_modifiers (BasicModifiers): экземпляр класса модификаторов характеристик персонажа;
        * self._class_hmsp (BasicHMSP): экземпляр класса, отвечающий за очки телесного/ментального здоровья, маны и стамины.

    Properties:
        * name - геттер, отвечающий за получение имени персонажа;
        * surname - геттер, отвечающий за получение фамилии персонажа;
        * fullname - геттер, отвечающий за получение имени и фамилии персонажа;
        * class_race - геттер, отвечающий за получение экземпляра класса расы персонажа;
        * class_profession - геттер, отвечающий за получение экземпляра класса профессии персонажа;
        * class_characteristics - геттер, отвечающий за получение экземпляра класса характеристик персонажа;
        * class_modifiers - геттер, отвечающий за получение экземпляра класса модификаторов характеристик персонажа;
        * class_hmsp - геттер, отвечающий за получение экземпляра класса модификаторов характеристик персонажа;

    Raises:
        * TypeError: Некорректный тип данных.

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
            name: str,
            surname: str,
            class_race: BasicRace,
            class_profession: BasicProfession,
            start_level: int = 1,
    ) -> None:

        self._name: str = name
        self._surname: str = surname
        self._fullname: str = f"{name} {surname}"
        self._class_race: BasicRace = class_race
        self._class_profession: BasicProfession = class_profession
        self._class_characteristics: BasicCharacteristics = BasicCharacteristics(
            class_race=self._class_race
        )

        self._class_modifiers: BasicModifiers = BasicModifiers(
            class_characteristics=self._class_characteristics
        )

        self._class_hmsp: BasicHMSP = BasicHMSP(
            class_profession=self._class_profession,
            class_modifiers=self._class_modifiers
        )

        self._class_level: BasicLevel = BasicLevel(start_level=start_level)
        self._class_proficiency_bonus: BasicProficiencyBonus = BasicProficiencyBonus(
            class_level=self._class_level
        )

        self._class_abilities_posessions: BasicAbilitiesPosessions = BasicAbilitiesPosessions(
            class_profession=self._class_profession
        )
        self._class_armors_posessions: BasicArmorsPosessions = BasicArmorsPosessions(
            class_profession=self._class_profession
        )
        self._class_common_tools_posessions: BasicCommonToolsPossessions = BasicCommonToolsPossessions(
            class_profession=self._class_profession
        )
        self._class_craft_tools_posessions: BasicCraftToolsPosessions = BasicCraftToolsPosessions(
            class_profession=self._class_profession
        )
        self._class_transport_posessions: BasicTransportPosessions = BasicTransportPosessions(
            class_profession=self._class_profession
        )
        self._class_weapons_posessions: BasicWeaponsPosessions = BasicWeaponsPosessions(
            class_profession=self._class_profession
        )

        self._class_abilities: BasicAbilities = BasicAbilities(
            class_modifiers=self._class_modifiers,
            class_proficiency_bonus=self._class_proficiency_bonus,
            class_abilities_posessions=self._class_abilities_posessions
        )


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def name(self) -> str:
        """
        Notes:
            Геттер, отвечающий за получение имени персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: имя персонажа.
        """

        Check.value_type(value=self._name, expected_type=str)
        return self._name

    @property
    def surname(self) -> str:
        """
        Notes:
            Геттер, отвечающий за получение фамилии персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: фамилия персонажа.
        """

        Check.value_type(value=self._surname, expected_type=str)
        return self._surname

    @property
    def fullname(self) -> str:
        """
        Notes:
            Геттер, отвечающий за получение имени и фамилии персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: имя и фамилия персонажа.
        """

        Check.value_type(value=self._fullname, expected_type=str)
        return self._fullname

    @property
    def class_race(self) -> BasicRace:
        """
        Notes:
            Геттер, отвечающий за получение экземпляра класса расы персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: экземпляр класса расы персонажа
        """

        Check.value_type(value=self._class_race, expected_type=BasicRace)
        return self._class_race

    @property
    def class_profession(self) -> BasicProfession:
        """
        Notes:
            Геттер, отвечающий за получение экземпляра класса профессии персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: экземпляр класса профессии персонажа
        """

        Check.value_type(value=self._class_profession, expected_type=BasicProfession)
        return self._class_profession

    @property
    def class_characteristics(self) -> BasicCharacteristics:
        """
        Notes:
            Геттер, отвечающий за получение экземпляра класса характеристик персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: экземпляр класса характеристик персонажа
        """

        Check.value_type(value=self._class_characteristics, expected_type=BasicCharacteristics)
        return self._class_characteristics

    @property
    def class_modifiers(self) -> BasicModifiers:
        """
        Notes:
            Геттер, отвечающий за получение экземпляра класса модификаторов характеристик персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: экземпляр класса модификаторов характеристик персонажа
        """

        Check.value_type(value=self._class_modifiers, expected_type=BasicModifiers)
        return self._class_modifiers

    @property
    def class_hmsp(self) -> BasicHMSP:
        """
        Notes:
            Геттер, отвечающий за получение экземпляра класса модификаторов характеристик персонажа.

        Raises:
            TypeError: Некорректный тип данных.

        Returns:
            str: экземпляр класса модификаторов характеристик персонажа
        """

        Check.value_type(value=self._class_hmsp, expected_type=BasicHMSP)
        return self._class_hmsp

    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
