# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
import random


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.professions.basic_profession import BasicProfession


# ##################################################
# КЛАССЫ
# ##################################################

class BasicAbilitiesPosessions:
    """
    Notes:
        Класс отвечает за владение навыками персонажа.

    Attributes:
        # СИЛА
        * self._athletics: bool - статус владения навыком (Атлетика);

        # ЛОВКОСТЬ
        * self._acrobatics: bool - статус владения навыком (Акробатика);
        * self._stealth: bool - статус владения навыком (Скрытность);
        * self._sleight_of_hands: bool - статус владения навыком (Ловкость рук);

        # ИНТЕЛЛЕКТ
        * self._analysis: bool - статус владения навыком (Анализ);
        * self._history: bool - статус владения навыком (История);
        * self._magic: bool - статус владения навыком (Магия);
        * self._nature: bool - статус владения навыком (Природа);
        * self._religion: bool - статус владения навыком (Религия);

        # МУДРОСТЬ
        * self._animal_care: bool - статус владения навыком (Забота о животных);
        * self._insight: bool - статус владения навыком (Проницательность);
        * self._medicine: bool - статус владения навыком (Медицина);
        * self._perception: bool - статус владения навыком (Восприятие);
        * self._survival: bool - статус владения навыком (Выживание);

        # ХАРИЗМА
        * self._deception: bool - статус владения навыком (Обман);
        * self._intimidation: bool - статус владения навыком (Запугивание);
        * self._performance: bool - статус владения навыком (Выступление);
        * self._persuasion: bool - статус владения навыком (Убеждение);

    Properties:
        * athletics - геттер и сеттер навыка (Атлетики);
        * acrobatics - геттер и сеттер навыка (Акробатика);
        * stealth - геттер и сеттер навыка (Скрытность);
        * sleight_of_hands - геттер и сеттер навыка (Ловкость рук);
        * analysis - геттер и сеттер навыка (Анализ);
        * history - геттер и сеттер навыка (История);
        * magic - геттер и сеттер навыка (Магия);
        * nature - геттер и сеттер навыка (Природа);
        * religion - геттер и сеттер навыка (Религия);
        * animal_care - геттер и сеттер навыка (Забота о животных);
        * insight - геттер и сеттер навыка (Проницательность);
        * medicine - геттер и сеттер навыка (Медицина);
        * perception - геттер и сеттер навыка (Восприятие);
        * survival - геттер и сеттер навыка (Выживание);
        * deception - геттер и сеттер навыка (Обман);
        * intimidation - геттер и сеттер навыка (Запугивание);
        * performance - геттер и сеттер навыка (Выступление);
        * persuasion - геттер и сеттер навыка (Убеждение);

    Raises:
        * TypeError: Некорректный тип данных.
        * ValueError: Некорректное наименование навыка;

    Methods:
        * random_choice_abilities - Метод принимает на вход целое число - количество навыков, которыми владеет персонаж на старте игры. Случайным образом выбирает n-ное количество навыков и присваивает им статус True (персонаж владеет данным навыком).
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

        # СИЛА
        self._athletics: bool = False

        # ЛОВКОСТЬ
        self._acrobatics: bool = False
        self._stealth: bool = False
        self._sleight_of_hands: bool = False

        # ИНТЕЛЛЕКТ
        self._analysis: bool = False
        self._history: bool = False
        self._magic: bool = False
        self._nature: bool = False
        self._religion: bool = False

        # МУДРОСТЬ
        self._animal_care: bool = False
        self._insight: bool = False
        self._medicine: bool = False
        self._perception: bool = False
        self._survival: bool = False

        # ХАРИЗМА
        self._deception: bool = False
        self._intimidation: bool = False
        self._performance: bool = False
        self._persuasion: bool = False

        if self._class_profession.available_abilities_posessions:
            self.choice_abilities_posessions()


    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    # ATHLETICS
    @property
    def athletics(self) -> bool:
        Check.value_type(value=self._athletics, expected_type=bool)
        return self._athletics

    @athletics.setter
    def athletics(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._athletics:
            self._athletics = value

    # ACROBATICS
    @property
    def acrobatics(self) -> bool:
        Check.value_type(value=self._acrobatics, expected_type=bool)
        return self._acrobatics

    @acrobatics.setter
    def acrobatics(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._acrobatics:
            self._acrobatics = value

    # STEALTH
    @property
    def stealth(self) -> bool:
        Check.value_type(value=self._stealth, expected_type=bool)
        return self._stealth

    @stealth.setter
    def stealth(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._stealth:
            self._stealth = value

    # SLEIGHT OF HANDS
    @property
    def sleight_of_hands(self) -> bool:
        Check.value_type(value=self._sleight_of_hands, expected_type=bool)
        return self._sleight_of_hands

    @sleight_of_hands.setter
    def sleight_of_hands(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._sleight_of_hands:
            self._sleight_of_hands = value

    # ANALYSIS
    @property
    def analysis(self) -> bool:
        Check.value_type(value=self._analysis, expected_type=bool)
        return self._analysis

    @analysis.setter
    def analysis(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._analysis:
            self._analysis = value

    # HISTORY
    @property
    def history(self) -> bool:
        Check.value_type(value=self._history, expected_type=bool)
        return self._history

    @history.setter
    def history(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._history:
            self._history = value

    # MAGIC
    @property
    def magic(self) -> bool:
        Check.value_type(value=self._magic, expected_type=bool)
        return self._magic

    @magic.setter
    def magic(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._magic:
            self._magic = value

    # NATURE
    @property
    def nature(self) -> bool:
        Check.value_type(value=self._nature, expected_type=bool)
        return self._nature

    @nature.setter
    def nature(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._nature:
            self._nature = value

    # RELIGION
    @property
    def religion(self) -> bool:
        Check.value_type(value=self._religion, expected_type=bool)
        return self._religion

    @religion.setter
    def religion(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._religion:
            self._religion = value

    # ANIMAL CARE
    @property
    def animal_care(self) -> bool:
        Check.value_type(value=self._animal_care, expected_type=bool)
        return self._animal_care

    @animal_care.setter
    def animal_care(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._animal_care:
            self._animal_care = value

    # INSIGHT
    @property
    def insight(self) -> bool:
        Check.value_type(value=self._insight, expected_type=bool)
        return self._insight

    @insight.setter
    def insight(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._insight:
            self._insight = value

    # MEDICINE
    @property
    def medicine(self) -> bool:
        Check.value_type(value=self._medicine, expected_type=bool)
        return self._medicine

    @medicine.setter
    def medicine(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._medicine:
            self._medicine = value

    # PERCEPTION
    @property
    def perception(self) -> bool:
        Check.value_type(value=self._perception, expected_type=bool)
        return self._perception

    @perception.setter
    def perception(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._perception:
            self._perception = value

    # SURVIVAL
    @property
    def survival(self) -> bool:
        Check.value_type(value=self._survival, expected_type=bool)
        return self._survival

    @survival.setter
    def survival(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._survival:
            self._survival = value

    # DECEPTION
    @property
    def deception(self) -> bool:
        Check.value_type(value=self._deception, expected_type=bool)
        return self._deception

    @deception.setter
    def deception(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._deception:
            self._deception = value

    # INTIMIDATION
    @property
    def intimidation(self) -> bool:
        Check.value_type(value=self._intimidation, expected_type=bool)
        return self._intimidation

    @intimidation.setter
    def intimidation(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._intimidation:
            self._intimidation = value

    # PERFORMANCE
    @property
    def performance(self) -> bool:
        Check.value_type(value=self._performance, expected_type=bool)
        return self._performance

    @performance.setter
    def performance(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._performance:
            self._performance = value

    # PERSUASION
    @property
    def persuasion(self) -> bool:
        Check.value_type(value=self._persuasion, expected_type=bool)
        return self._persuasion

    @persuasion.setter
    def persuasion(self, value: bool) -> None:
        Check.value_type(value=value, expected_type=bool)
        if value != self._persuasion:
            self._persuasion = value


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def choice_abilities_posessions(self) -> None:
        """
        Notes:
            Метод обращается к экземпляру класса Профессии и считывает данные о количестве стартовых навыков, которыми владеет персонаж его профессии, а так же множество доступных навыков.

        Raises:
            ValueError: Некорректное наименование навыка;
            TypeError: Некорректный тип данных.
        """

        for _ in range(self._class_profession.count_start_abilities_posessions):
            Check.value_type(
                value=self._class_profession.available_abilities_posessions,
                expected_type=list
            )
            available_abilities: list[str] = self._class_profession.available_abilities_posessions.copy()

            abilitie: str = random.choice(seq=available_abilities)
            Check.value_type(value=abilitie, expected_type=str)

            available_abilities.remove(abilitie)

            match abilitie:
                case "athletics":
                    self._athletics = True

                case "acrobatics":
                    self._acrobatics = True

                case "stealth":
                    self._stealth = True

                case "sleight_of_hands":
                    self._sleight_of_hands = True

                case "analysis":
                    self._analysis = True

                case "history":
                    self._history = True

                case "magic":
                    self._magic = True

                case "nature":
                    self._nature = True

                case "religion":
                    self._religion = True

                case "animal_care":
                    self._animal_care = True

                case "insight":
                    self._insight = True

                case "medicine":
                    self._medicine = True

                case "perception":
                    self._perception = True

                case "survival":
                    self._survival = True

                case "deception":
                    self._deception = True

                case "intimidation":
                    self._intimidation = True

                case "performance":
                    self._performance = True

                case "persuasion":
                    self._persuasion = True

                case _:
                    raise ValueError("Некорректное наименование навыка;")
