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

class BasicProfession:
    """
    Notes:
        Родительский класс для игровых профессий.

    Attributes:
        * _available_professions (dict[str, str]): словарь с наименованиями доступных игровых профессий;
        * self._name: str = "Родительский класс игровых профессий";
        * self._health_points_dice (int): кубик, отвечающий за очки телесного здоровья. По умолчанию 6;
        * self._mind_points_dice (int): кубик, отвечающий за очки ментального здоровья. По умолчанию 6;
        * self._mana_points_dice (int): кубик, отвечающий за очки маны. По умолчанию 6;
        * self._stamina_points_dice (int): кубик, отвечающий за очки стамины. По умолчанию 6;

    Properties:
        * name - геттер, отвечающий за получение наименования Профессии;
        * health_points_dice - геттер, отвечающий за получение значение кубика, отвечающего за очки телесного здоровья;
        * mind_points_dice - геттер, отвечающий за получение значение кубика, отвечающего за очки ментального здоровья;
        * mana_points_dice - геттер, отвечающий за получение значение кубика, отвечающего за очки маны;
        * stamina_points_dice - геттер, отвечающий за получение значение кубика, отвечающего за очки стамины;

    Raises:
        * TypeError: некорректный тип данных;

    Methods:
        ...
    """

    # ##################################################
    # 1. АТРИБУТЫ КЛАССА
    # ##################################################
    _available_professions: dict[str, str] = {
        "Воин": "Warrior",
        "Следопыт": "Rouge",
        "Маг": "Wizard"
    }

    # ВЛАДЕНИЯ
    _count_start_abilities_posessions: int = 0
    _available_abilities_posessions: list[str] = [
        "acrobatics",
        "analysis",
        "animal_care",
        "athletics",
        "deception",
        "history",
        "insight",
        "intimidation",
        "magic",
        "medicine",
        "nature",
        "perception",
        "performance",
        "persuasion",
        "religion",
        "sleight_of_hands",
        "stealth",
        "survival"
    ]

    _available_armor_posessions: list[str] = [
        "light_armor",
        "medium_armor",
        "heavy_armor",
        "shield"
    ]

    _available_common_tools_posessions: list[str] = [
        "disguise_kit",
        "forgery_kit",
        "gaming_set",
        "herbalism_kit",
        "musical_instruments",
        "navigator_tools",
        "poisoners_kit",
        "thieves_tools"
    ]

    _available_craft_tools_posessions: list[str] = [
        "alchemists_supplies",
        "artisans_tools",
        "brewer_tools",
        "calligraphers_supplies",
        "carpenter_tools",
        "cartographer_tools",
        "cobblers_tools",
        "cooks_utensils",
        "glass_blower_tools",
        "jeweler_tools",
        "letherworker_tools",
        "masons_tools",
        "painters_supplies",
        "potter_tools",
        "smiths_tools",
        "tinkers_tools",
        "weaver_tools",
        "wood_carver_tools"
    ]

    _available_transport_posessions: list[str] = [
        "donkey",
        "hourse",
        "wagon",
        "carriage",
        "boat",
        "sailboat",
        "ship",
        "warship",
        "aerostat"
    ]

    _available_weapon_posessions: list[str] = [
        "staff",
        "dagger",
        "sword",
        "bow",
        "crossbow"
    ]


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
    def __init__(self) -> None:
        # БАЗОВАЯ ИНФОРМАЦИЯ
        self._name: str = "Родительский класс игровых профессий"

        # КОСТИ ОЧКОВ
        self._health_points_dice: int = 6
        self._mind_points_dice: int = 6
        self._mana_points_dice: int = 6
        self._stamina_points_dice: int = 6


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def name(self) -> str:
        Check.value_type(value=self._name, expected_type=str)
        return self._name

    @property
    def health_points_dice(self) -> int:
        Check.value_type(value=self._health_points_dice, expected_type=int)
        return self._health_points_dice

    @property
    def mind_points_dice(self) -> int:
        Check.value_type(value=self._mind_points_dice, expected_type=int)
        return self._mind_points_dice

    @property
    def mana_points_dice(self) -> int:
        Check.value_type(value=self._mana_points_dice, expected_type=int)
        return self._mana_points_dice

    @property
    def stamina_points_dice(self) -> int:
        Check.value_type(value=self._stamina_points_dice, expected_type=int)
        return self._stamina_points_dice

    # ВЛАДЕНИЯ
    @property
    def count_start_abilities_posessions(self) -> int:
        Check.value_type(value=self._count_start_abilities_posessions, expected_type=int)
        return self._count_start_abilities_posessions

    @property
    def available_abilities_posessions(self) -> list[str]:
        Check.value_type(value=self._available_abilities_posessions, expected_type=list)
        return self._available_abilities_posessions

    @property
    def available_armor_posessions(self) -> list[str]:
        Check.value_type(value=self._available_armor_posessions, expected_type=list)
        return self._available_armor_posessions

    @property
    def available_common_tools_posessions(self) -> list[str]:
        Check.value_type(value=self._available_common_tools_posessions, expected_type=list)
        return self._available_common_tools_posessions

    @property
    def available_craft_tools_posessions(self) -> list[str]:
        Check.value_type(value=self._available_craft_tools_posessions, expected_type=list)
        return self._available_craft_tools_posessions

    @property
    def available_transport_posessions(self) -> list[str]:
        Check.value_type(value=self._available_transport_posessions, expected_type=list)
        return self._available_transport_posessions

    @property
    def available_weapon_posessions(self) -> list[str]:
        Check.value_type(value=self._available_weapon_posessions, expected_type=list)
        return self._available_weapon_posessions


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
