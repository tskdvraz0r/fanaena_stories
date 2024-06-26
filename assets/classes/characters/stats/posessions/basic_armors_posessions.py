# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.professions.basic_profession import BasicProfession


# ##################################################
# КЛАССЫ
# ##################################################

class BasicArmorsPosessions:
    """
    Notes:
        Класс отвечает за владение броней.

    Attributes:
        * class_profession: BasicProfession - экземпляр класса "Профессии" персонажа;
        * _light_armor: bool - владение лёгкой бронёй;
        * _medium_armor: bool - владение средней бронёй;
        * _heavy_armor: bool - владение тяжёлой бронёй;
        * _shield: bool - владение щитом;

    Properties:
        * light_armor - геттер и сеттер владения легкой бронёй;
        * medium_armor - геттер и сеттер владения средней бронёй;
        * heavy_armor - геттер и сеттер владения тяжёлой бронёй;
        * shield - геттер и сеттер владения щитом;

    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * choice_armor_posessions - Метод считывает из экземпляра класса Профессии данные по владению доспехами и меняет статус с False на True.
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
            class_profession: BasicProfession
    ) -> None:
        Check.value_type(value=class_profession, expected_type=BasicProfession)
        self._class_profession: BasicProfession = class_profession

        self._light_armor: bool = False
        self._medium_armor: bool = False
        self._heavy_armor: bool = False
        self._shield: bool = False

        if self._class_profession.available_armor_posessions:
            self.choice_armor_posessions()


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    # LIGHT ARMOR
    @property
    def light_armor(self) -> bool:
        Check.value_type(value=self._light_armor, expected_type=bool)
        return self._light_armor

    @light_armor.setter
    def light_armor(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._light_armor:
            self._light_armor = value

    # MEDIUM ARMOR
    @property
    def medium_armor(self) -> bool:
        Check.value_type(value=self._medium_armor, expected_type=bool)
        return self._medium_armor

    @medium_armor.setter
    def medium_armor(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._medium_armor:
            self._medium_armor = value

    # HEAVY ARMOR
    @property
    def heavy_armor(self) -> bool:
        Check.value_type(value=self._heavy_armor, expected_type=bool)
        return self._heavy_armor

    @heavy_armor.setter
    def heavy_armor(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._heavy_armor:
            self._heavy_armor = value

    # SHILD
    @property
    def shield(self) -> bool:
        Check.value_type(value=self._shield, expected_type=bool)
        return self._shield

    @shield.setter
    def shield(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._shield:
            self._shield = value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def choice_armor_posessions(self) -> None:
        """
        Notes:
            Метод считывает из экземпляра класса Профессии данные по владению доспехами и меняет статус с False на True.

        Raises:
            TypeError: Некорректный тип данных;
            ValueError: Некорректный тип брони;
        """

        Check.value_type(
            value=self._class_profession.available_armor_posessions,
            expected_type=list
        )

        for armor in self._class_profession.available_armor_posessions:
            Check.value_type(value=armor, expected_type=str)

            match armor:
                case "light_armor":
                    self._light_armor = True

                case "medium_armor":
                    self._medium_armor = True

                case "heavy_armor":
                    self._heavy_armor = True

                case "shield":
                    self._shield = True

                case _:
                    raise ValueError("Некорректный тип брони;")
