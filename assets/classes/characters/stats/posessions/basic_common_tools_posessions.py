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

class BasicCommonToolsPossessions:
    """
    Notes:
        Класс отвечает за владения персонажем обычными инструментами.

    Attributes:
        * class_profession: BasicProfession - экземпляр класса "Профессии" персонажа;
        * self._disguise_kit: bool - владение набором для грима;
        * self._forgery_kit: bool - владение набором для фальсификации;
        * self._gaming_set: bool - владение игровым набором;
        * self._herbalism_kit: bool - владение набором травника;
        * self._musical_instruments: bool - владение музыкальными инструментами;
        * self._navigator_tools: bool - владение инструментами картографа;
        * self._poisoners_kit: bool - владение инструментами отравителя;
        * self._thieves_tools: bool - владение воровскими инструментами;

    Properties:
        * disguise_kit - геттер и сеттер;
        * forgery_kit - геттер и сеттер;
        * gaming_set - геттер и сеттер;
        * herbalism_kit - геттер и сеттер;
        * musical_instruments - геттер и сеттер;
        * navigator_tools - геттер и сеттер;
        * poisoners_kit - геттер и сеттер;
        * thieves_tools - геттер и сеттер;

    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * choice_common_tools_posessions - Метод считывает из экземпляра класса Профессии данные по владению обычными инструментами и меняет статус с False на True.
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

        self._disguise_kit: bool = False
        self._forgery_kit: bool = False
        self._gaming_set: bool = False
        self._herbalism_kit: bool = False
        self._musical_instruments: bool = False
        self._navigator_tools: bool = False
        self._poisoners_kit: bool = False
        self._thieves_tools: bool = False

        if self._class_profession.available_common_tools_posessions:
            self.choice_common_tools_posessions()


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    # DISGUISE KIT
    @property
    def disguise_kit(self) -> bool:
        Check.value_type(value=self._disguise_kit, expected_type=bool)
        return self._disguise_kit

    @disguise_kit.setter
    def disguise_kit(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._disguise_kit:
            self._disguise_kit = value

    # FORGERY KIT
    @property
    def forgery_kit(self) -> bool:
        Check.value_type(value=self._forgery_kit, expected_type=bool)
        return self._forgery_kit

    @forgery_kit.setter
    def forgery_kit(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._forgery_kit:
            self._forgery_kit = value

    # GAMING SET
    @property
    def gaming_set(self) -> bool:
        Check.value_type(value=self._gaming_set, expected_type=bool)
        return self._gaming_set

    @gaming_set.setter
    def gaming_set(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._gaming_set:
            self._gaming_set = value

    # HERBALISM KIT
    @property
    def herbalism_kit(self) -> bool:
        Check.value_type(value=self._herbalism_kit, expected_type=bool)
        return self._herbalism_kit

    @herbalism_kit.setter
    def herbalism_kit(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._herbalism_kit:
            self._herbalism_kit = value

    # MUSICAL INSTRUMENTS
    @property
    def musical_instruments(self) -> bool:
        Check.value_type(value=self._musical_instruments, expected_type=bool)
        return self._musical_instruments

    @musical_instruments.setter
    def musical_instruments(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._musical_instruments:
            self._musical_instruments = value

    # NAVIGATOR TOOLS
    @property
    def navigator_tools(self) -> bool:
        Check.value_type(value=self._navigator_tools, expected_type=bool)
        return self._navigator_tools

    @navigator_tools.setter
    def navigator_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._navigator_tools:
            self._navigator_tools = value

    # POISONERS KIT
    @property
    def poisoners_kit(self) -> bool:
        Check.value_type(value=self._poisoners_kit, expected_type=bool)
        return self._poisoners_kit

    @poisoners_kit.setter
    def poisoners_kit(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._poisoners_kit:
            self._poisoners_kit = value

    # THIEVES TOOLS
    @property
    def thieves_tools(self) -> bool:
        Check.value_type(value=self._thieves_tools, expected_type=bool)
        return self._thieves_tools

    @thieves_tools.setter
    def thieves_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._thieves_tools:
            self._thieves_tools = value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def choice_common_tools_posessions(self) -> None:
        """
        Notes:
            Метод считывает из экземпляра класса Профессии данные по владению обычными инструментами и меняет статус с False на True.

        Raises:
            TypeError: Некорректный тип данных;
            ValueError: Некорректный тип брони;
        """

        Check.value_type(
            value=self._class_profession.available_common_tools_posessions,
            expected_type=list
        )

        for common_tools in self._class_profession.available_common_tools_posessions:
            Check.value_type(value=common_tools, expected_type=str)

            match common_tools:
                case "disguise_kit":
                    self._disguise_kit = True

                case "forgery_kit":
                    self._forgery_kit = True

                case "gaming_set":
                    self._gaming_set = True

                case "herbalism_kit":
                    self._herbalism_kit = True

                case "musical_instruments":
                    self._musical_instruments = True

                case "navigator_tools":
                    self._navigator_tools = True

                case "poisoners_kit":
                    self._poisoners_kit = True

                case "thieves_tools":
                    self._thieves_tools = True

                case _:
                    raise ValueError("Некорректный тип обычных инструментов;")
