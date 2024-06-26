# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
from assets.classes.characters.professions.basic_profession import BasicProfession


# Проектные библиотеки
...

# ##################################################
# КЛАССЫ
# ##################################################

class WizardProfession(BasicProfession):
    """
    Notes:
        Родительский класс для игровых профессий.

    Attributes:
        * _available_professions (dict[str, str]): словарь с наименованиями доступных игровых профессий;
        * self._name: str = "Волшебник";
        * self._health_points_dice (int): кубик, отвечающий за очки телесного здоровья. По умолчанию 10;
        * self._mind_points_dice (int): кубик, отвечающий за очки ментального здоровья. По умолчанию 6;
        * self._mana_points_dice (int): кубик, отвечающий за очки маны. По умолчанию 4;
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
        super().__init__()

        self._name: str = "Волшебник"
        self._mind_points_dice: int = 10
        self._mana_points_dice: int = 8


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
