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

class BasicTransportPosessions:
    """
    Notes:
        Класс отвечает за владения персонажем транспортом.

    Attributes:
        # СУХОПУТНЫЙ ТРАНСПОРТ
        * self._donkey: bool - владение ездой верхом на осле;
        * self._hourse: bool - владение ездой верхом на лошади;
        * self._wagon: bool - владение управлением повозкой, телегой...;
        * self._carriage: bool - владение управлением каретой;

        # ВОДНЫЙ ТРАНСПОРТ
        * self._boat: bool - владение управлением вёсельной лодкой;
        * self._sailboat: bool - владение управлением парусной лодкой;
        * self._ship: bool - владение управлением кораблём;
        * self._warship: bool - владение управлением боевым кораьлём;

        # ВОЗДУШНЫЙ ТРАНСПОРТ
        * self._aerostat: bool - владение управлением аэростатом (воздушным шаром);

    Properties:
        * donkey - геттер и сеттер владения верховой ездой на осле;
        * hourse - геттер и сеттер владения верховой ездой на лошади;
        * wagon - геттер и сеттер владения управлением повозкой, телегой...;
        * carriage - геттер и сеттер владения управлением каретой;
        * boat - геттер и сеттер владения управлением вёсельной лодкой;
        * sailboat - геттер и сеттер владения управлением парусной лодкой
        * ship - геттер и сеттер владения управлением кораблём;
        * warship - геттер и сеттер владения управлением боевым кораблём;
        * aerostat - геттер и сеттер владения управлением аэростатом (воздушным шаром);

    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * choice_transport_posessions - Метод считывает из экземпляра класса Профессии данные по владению навыками управления транспортом и меняет статус с False на True.
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

        # СУХОПУТНЫЙ ТРАНСПОРТ
        self._donkey: bool = False
        self._hourse: bool = False
        self._wagon: bool = False
        self._carriage: bool = False

        # ВОДНЫЙ ТРАНСПОРТ
        self._boat: bool = False
        self._sailboat: bool = False
        self._ship: bool = False
        self._warship: bool = False

        # ВОЗДУШНЫЙ ТРАНСПОРТ
        self._aerostat: bool = False

        if self._class_profession.available_transport_posessions:
            self.choice_transport_posessions()

    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    # СУХОПУТНЫЙ ТРАНСПОРТ
    ## DONKEY
    @property
    def donkey(self) -> bool:
        Check.value_type(value=self._donkey, expected_type=bool)
        return self._donkey

    @donkey.setter
    def donkey(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._donkey:
            self._donkey = value

    ## HOURSE
    @property
    def hourse(self) -> bool:
        Check.value_type(value=self._hourse, expected_type=bool)
        return self._hourse

    @hourse.setter
    def hourse(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._hourse:
            self._hourse = value

    ## WAGON
    @property
    def wagon(self) -> bool:
        Check.value_type(value=self._wagon, expected_type=bool)
        return self._wagon

    @wagon.setter
    def wagon(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._wagon:
            self._wagon = value

    ## CARRIAGE
    @property
    def carriage(self) -> bool:
        Check.value_type(value=self._carriage, expected_type=bool)
        return self._carriage

    @carriage.setter
    def carriage(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._carriage:
            self._carriage = value


    # ВОДНЫЙ ТРАНСПОРТ
    ## DONKEY
    @property
    def boat(self) -> bool:
        Check.value_type(value=self._boat, expected_type=bool)
        return self._boat

    @boat.setter
    def boat(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._boat:
            self._boat = value

    ## SAILBOAT
    @property
    def sailboat(self) -> bool:
        Check.value_type(value=self._sailboat, expected_type=bool)
        return self._sailboat

    @sailboat.setter
    def sailboat(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._sailboat:
            self._sailboat = value

    ## SHIP
    @property
    def ship(self) -> bool:
        Check.value_type(value=self._ship, expected_type=bool)
        return self._ship

    @ship.setter
    def ship(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._ship:
            self._ship = value

    ## WARSHIP
    @property
    def warship(self) -> bool:
        Check.value_type(value=self._warship, expected_type=bool)
        return self._warship

    @warship.setter
    def warship(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._warship:
            self._warship = value


    # ВОЗДУШНЫЙ ТРАНСПОРТ
    ## AEROSTAT
    @property
    def aerostat(self) -> bool:
        Check.value_type(value=self._aerostat, expected_type=bool)
        return self._aerostat

    @aerostat.setter
    def aerostat(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._aerostat:
            self._aerostat = value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def choice_transport_posessions(self) -> None:
        """
        Notes:
            Метод считывает из экземпляра класса Профессии данные по владению навыками управления транспортом и меняет статус с False на True.

        Raises:
            TypeError: Некорректный тип данных;
            ValueError: Некорректный тип транспорта;
        """

        Check.value_type(
            value=self._class_profession.available_transport_posessions,
            expected_type=list
        )

        for transport in self._class_profession.available_transport_posessions:
            Check.value_type(value=transport, expected_type=str)

            match transport:
                case "donkey":
                    self._donkey = True

                case "hourse":
                    self._hourse = True

                case "wagon":
                    self._wagon = True

                case "carriage":
                    self._carriage = True

                case "boat":
                    self._boat = True

                case "sailboat":
                    self._sailboat = True

                case "ship":
                    self.ship = True

                case "warship":
                    self._warship = True

                case "aerostat":
                    self._aerostat = True

                case _:
                    raise ValueError("Некорректный тип транспорта;")
