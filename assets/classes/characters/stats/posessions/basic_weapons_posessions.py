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

class BasicWeaponsPosessions:
    """
    Notes:
        Класс отвечает за владения персонажем оружием.

    Attributes:
        * class_profession: BasicProfession - экземпляр класса "Профессии" персонажа;
        * self._staff: bool - владение посохом / палкой;
        * self._dagger: bool - владение кинжалом;
        * self._sword: bool - владение мечём;
        * self._bow: bool - владение луком;
        * self._crossbow: bool - владение арбалетом;

    Properties:
        * staff - геттер и сеттер;
        * dagger - геттер и сеттер;
        * sword - геттер и сеттер;
        * bow - геттер и сеттер;
        * crossbow - геттер и сеттер;


    Raises:
        * TypeError: Некорректный тип данных.

    Methods:
        * choice_weapon_posessions - Метод считывает из экземпляра класса Профессии данные по владению оружием и меняет статус с False на True.
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

        self._staff: bool = False
        self._dagger: bool = False
        self._sword: bool = False
        self._bow: bool = False
        self._crossbow: bool = False

        if self._class_profession.available_weapon_posessions:
            self.choice_weapon_posessions()


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    # STAFF
    @property
    def staff(self) -> bool:
        Check.value_type(value=self._staff, expected_type=bool)
        return self._staff

    @staff.setter
    def staff(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._staff:
            self._staff = value

    # DAGGER
    @property
    def dagger(self) -> bool:
        Check.value_type(value=self._dagger, expected_type=bool)
        return self._dagger

    @dagger.setter
    def dagger(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._dagger:
            self._dagger = value

    # SWORD
    @property
    def sword(self) -> bool:
        Check.value_type(value=self._sword, expected_type=bool)
        return self._sword

    @sword.setter
    def sword(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._sword:
            self._sword = value

    # BOW
    @property
    def bow(self) -> bool:
        Check.value_type(value=self._bow, expected_type=bool)
        return self._bow

    @bow.setter
    def bow(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._bow:
            self._bow = value

    # CROSSBOW
    @property
    def crossbow(self) -> bool:
        Check.value_type(value=self._crossbow, expected_type=bool)
        return self._crossbow

    @crossbow.setter
    def donkey(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._crossbow:
            self._crossbow = value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def choice_weapon_posessions(self) -> None:
        """
        Notes:
            Метод считывает из экземпляра класса Профессии данные по владению оружием и меняет статус с False на True.

        Raises:
            TypeError: Некорректный тип данных;
            ValueError: Некорректный тип оружия;
        """

        Check.value_type(
            value=self._class_profession.available_weapon_posessions,
            expected_type=list
        )

        for weapon in self._class_profession.available_weapon_posessions:
            Check.value_type(value=weapon, expected_type=str)

            match weapon:
                case "staff":
                    self._staff = True

                case "dagger":
                    self._dagger = True

                case "sword":
                    self._sword = True

                case "bow":
                    self._bow = True

                case "crossbow":
                    self._crossbow = True

                case _:
                    raise ValueError("Некорректный тип оружия;")
