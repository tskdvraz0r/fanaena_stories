# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...

# Сторонние библиотеки
...

# Проектные библиотеки
from classes.character.races import Race
from classes.character.professions import Profession
from classes.character.characteristics import Characteristics
from classes.character.modifiers import Modifiers
from classes.character.hmsp import HMSP


# ##################################################
# КЛАССЫ
# ##################################################

class Character:
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
            name: str,
            surname: str,
            class_race: Race,
            class_profession: Profession
    ) -> None:
        
        self._name: str = name
        self._surname: str = surname
        self._fullname: str = f"{name} {surname}"

        self._class_race: Race = class_race
        self._class_profession: Profession = class_profession

        self._class_characteristics: Characteristics = Characteristics(
            class_race=self._class_race
        )

        self._class_modifiers: Modifiers = Modifiers(
            class_characteristics=self._class_characteristics
        )

        self._class_hmsp: HMSP = HMSP(
            class_profession=self._class_profession,
            class_modifiers=self._class_modifiers
        )


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
