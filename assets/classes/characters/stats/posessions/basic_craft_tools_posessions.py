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

class BasicCraftToolsPosessions:
    """
    Notes:
        Класс отвечает за владения персонажем инструментами ремесленника.

    Attributes:
        * class_profession: BasicProfession - экземпляр класса "Профессии" персонажа;
        * self._alchemists_supplies: bool - владение инструментами алхимика;
        * self._artisans_tools: bool - владение инструментами ремесленника;
        * self._brewer_tools: bool - владение инструментами пивовара;
        * self._calligraphers_supplies: bool - владение инструментами каллиграфа;
        * self._carpenter_tools: bool - владение инструментами плотника;
        * self._cartographer_tools: bool - владение инструментами картографа;
        * self._cobblers_tools: bool - владение инструментами сапожника;
        * self._cooks_utensils: bool - владение инструментами повара;
        * self._glass_blower_tools: bool - владение инструментами стеклодува;
        * self._jeweler_tools: bool - владение инструментами ювелира;
        * self._letherworker_tools: bool - владение инструментами кожевника;
        * self._masons_tools: bool - владение инструментами каменщика;
        * self._painters_supplies: bool - владение инструментами художника;
        * self._potter_tools: bool - владение инструментами гончара;
        * self._smiths_tools: bool - владение инструментами кузнеца;
        * self._tinkers_tools: bool - владение инструментами ремонтника;
        * self._weaver_tools: bool - владение инструментами ткача;
        * self._wood_carver_tools: bool - владение инструментами резчика по дереву;

    Properties:
        * alchemists_supplies - геттер и сеттер;
        * artisans_tools - геттер и сеттер;
        * brewer_tools - геттер и сеттер;
        * calligraphers_supplies - геттер и сеттер;
        * carpenter_tools - геттер и сеттер;
        * cartographer_tools - геттер и сеттер;
        * cobblers_tools - геттер и сеттер;
        * cooks_utensils - геттер и сеттер;
        * glass_blower_tools - геттер и сеттер;
        * jeweler_tools - геттер и сеттер;
        * letherworker_tools - геттер и сеттер;
        * masons_tools - геттер и сеттер;
        * painters_supplies - геттер и сеттер;
        * potter_tools - геттер и сеттер;
        * smiths_tools - геттер и сеттер;
        * tinkers_tools - геттер и сеттер;
        * weaver_tools - геттер и сеттер;
        * wood_carver_tools - геттер и сеттер;

    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * choice_craft_tools_posessions - Метод считывает из экземпляра класса Профессии данные по владению инструментами ремесленника и меняет статус с False на True.
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

        self._alchemists_supplies: bool = False
        self._artisans_tools: bool = False
        self._brewer_tools: bool = False
        self._calligraphers_supplies: bool = False
        self._carpenter_tools: bool = False
        self._cartographer_tools: bool = False
        self._cobblers_tools: bool = False
        self._cooks_utensils: bool = False
        self._glass_blower_tools: bool = False
        self._jeweler_tools: bool = False
        self._letherworker_tools: bool = False
        self._masons_tools: bool = False
        self._painters_supplies: bool = False
        self._potter_tools: bool = False
        self._smiths_tools: bool = False
        self._tinkers_tools: bool = False
        self._weaver_tools: bool = False
        self._wood_carver_tools: bool = False


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    # ALCHEMISTS SUPPLIES
    @property
    def alchemists_supplies(self) -> bool:
        Check.value_type(value=self._alchemists_supplies, expected_type=bool)
        return self._alchemists_supplies

    @alchemists_supplies.setter
    def alchemists_supplies(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._alchemists_supplies:
            self._alchemists_supplies = value

    # ARTISANS TOOLS
    @property
    def artisans_tools(self) -> bool:
        Check.value_type(value=self._artisans_tools, expected_type=bool)
        return self._artisans_tools

    @artisans_tools.setter
    def artisans_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._artisans_tools:
            self._artisans_tools = value

    # BREWER TOOLS
    @property
    def brewer_tools(self) -> bool:
        Check.value_type(value=self._brewer_tools, expected_type=bool)
        return self._brewer_tools

    @brewer_tools.setter
    def brewer_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._brewer_tools:
            self._brewer_tools = value

    # CALLIGRAPHERS SUPPLIES
    @property
    def calligraphers_supplies(self) -> bool:
        Check.value_type(value=self._calligraphers_supplies, expected_type=bool)
        return self._calligraphers_supplies

    @calligraphers_supplies.setter
    def calligraphers_supplies(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._calligraphers_supplies:
            self._calligraphers_supplies = value

    # CARPENTER TOOLS
    @property
    def carpenter_tools(self) -> bool:
        Check.value_type(value=self._carpenter_tools, expected_type=bool)
        return self._carpenter_tools

    @carpenter_tools.setter
    def carpenter_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._carpenter_tools:
            self._carpenter_tools = value

    # CARTOGRAPHER TOOLS
    @property
    def cartographer_tools(self) -> bool:
        Check.value_type(value=self._cartographer_tools, expected_type=bool)
        return self._cartographer_tools

    @cartographer_tools.setter
    def cartographer_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._cartographer_tools:
            self._cartographer_tools = value

    # COBBLERS TOOLS
    @property
    def cobblers_tools(self) -> bool:
        Check.value_type(value=self._cobblers_tools, expected_type=bool)
        return self._cobblers_tools

    @cobblers_tools.setter
    def cobblers_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._cobblers_tools:
            self._cobblers_tools = value

    # COOKS UTENSILS
    @property
    def cooks_utensils(self) -> bool:
        Check.value_type(value=self._cooks_utensils, expected_type=bool)
        return self._cooks_utensils

    @cooks_utensils.setter
    def cooks_utensils(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._cooks_utensils:
            self._cooks_utensils = value

    # GLASS BLOWER TOOLS
    @property
    def glass_blower_tools(self) -> bool:
        Check.value_type(value=self._glass_blower_tools, expected_type=bool)
        return self._glass_blower_tools

    @glass_blower_tools.setter
    def glass_blower_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._glass_blower_tools:
            self._glass_blower_tools = value

    # JEWELER TOOLS
    @property
    def jeweler_tools(self) -> bool:
        Check.value_type(value=self._jeweler_tools, expected_type=bool)
        return self._jeweler_tools

    @jeweler_tools.setter
    def jeweler_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._jeweler_tools:
            self._jeweler_tools = value

    # LETHERWORKER TOOLS
    @property
    def letherworker_tools(self) -> bool:
        Check.value_type(value=self._letherworker_tools, expected_type=bool)
        return self._letherworker_tools

    @letherworker_tools.setter
    def letherworker_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._letherworker_tools:
            self._letherworker_tools = value

    # MASONS TOOLS
    @property
    def masons_tools(self) -> bool:
        Check.value_type(value=self._masons_tools, expected_type=bool)
        return self._masons_tools

    @masons_tools.setter
    def masons_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._masons_tools:
            self._masons_tools = value

    # PAINTERS SUPPLIES
    @property
    def painters_supplies(self) -> bool:
        Check.value_type(value=self._painters_supplies, expected_type=bool)
        return self._painters_supplies

    @painters_supplies.setter
    def painters_supplies(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._painters_supplies:
            self._painters_supplies = value

    # POTTER TOOLS
    @property
    def potter_tools(self) -> bool:
        Check.value_type(value=self._potter_tools, expected_type=bool)
        return self._potter_tools

    @potter_tools.setter
    def potter_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._potter_tools:
            self._potter_tools = value

    # SMITHS TOOLS
    @property
    def smiths_tools(self) -> bool:
        Check.value_type(value=self._smiths_tools, expected_type=bool)
        return self._smiths_tools

    @smiths_tools.setter
    def smiths_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._smiths_tools:
            self._smiths_tools = value

    # TINKERS TOOLS
    @property
    def tinkers_tools(self) -> bool:
        Check.value_type(value=self._tinkers_tools, expected_type=bool)
        return self._tinkers_tools

    @tinkers_tools.setter
    def tinkers_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._tinkers_tools:
            self._tinkers_tools = value

    # WEAVER TOOLS
    @property
    def weaver_tools(self) -> bool:
        Check.value_type(value=self._weaver_tools, expected_type=bool)
        return self._weaver_tools

    @weaver_tools.setter
    def weaver_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._weaver_tools:
            self._weaver_tools = value

    # WOOD CARVER TOOLS
    @property
    def wood_carver_tools(self) -> bool:
        Check.value_type(value=self._wood_carver_tools, expected_type=bool)
        return self._wood_carver_tools

    @wood_carver_tools.setter
    def wood_carver_tools(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._wood_carver_tools:
            self._wood_carver_tools = value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def choice_craft_tools_posessions(self) -> None:
        """
        Notes:
            Метод считывает из экземпляра класса Профессии данные по владению инструментами ремесленника и меняет статус с False на True.

        Raises:
            TypeError: Некорректный тип данных;
            ValueError: Некорректный тип инструмента ремесленника;
        """

        Check.value_type(
            value=self._class_profession.available_craft_tools_posessions,
            expected_type=list
        )

        for craft_tools in self._class_profession.available_craft_tools_posessions:
            Check.value_type(value=craft_tools, expected_type=str)

            match craft_tools:
                case "alchemists_supplies":
                    self._alchemists_supplies = True

                case "artisans_tools":
                    self._artisans_tools = True

                case "brewer_tools":
                    self._brewer_tools = True

                case "calligraphers_supplies":
                    self._calligraphers_supplies = True

                case "carpenter_tools":
                    self._carpenter_tools = True

                case "cartographer_tools":
                    self._cartographer_tools = True

                case "cobblers_tools":
                    self._cobblers_tools = True

                case "cooks_utensils":
                    self._cooks_utensils = True

                case "glass_blower_tools":
                    self._glass_blower_tools = True

                case "jeweler_tools":
                    self._jeweler_tools = True

                case "letherworker_tools":
                    self._letherworker_tools = True

                case "masons_tools":
                    self._masons_tools = True

                case "painters_supplies":
                    self._painters_supplies = True

                case "potter_tools":
                    self._potter_tools = True

                case "smiths_tools":
                    self._smiths_tools = True

                case "tinkers_tools":
                    self._tinkers_tools = True

                case "weaver_tools":
                    self._weaver_tools = True

                case "wood_carver_tools":
                    self._wood_carver_tools = True

                case _:
                    raise ValueError("Некорректный тип инструмента ремесленника;")
