# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
...


# Сторонние библиотеки
...


# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.stats.modifiers.basic_modifiers import BasicModifiers
from assets.classes.characters.stats.proficiency_bonus.basic_proficiency_bonus import BasicProficiencyBonus
from assets.classes.characters.stats.posessions.basic_abilities_posessions import BasicAbilitiesPosessions


# ##################################################
# КЛАССЫ
# ##################################################

class BasicAbilities:
    """
    Notes:
        Класс отвечает за способности персонажа.

    Attributes:
        # СИЛА
        * self._athletics (int): Атлетика - (Сила) навык отвечает за следующие проверки: бег, прыжки, плавание и лазание;

        # ЛОВКОСТЬ
        * self._acrobatics (int): Акробатика - (Ловкость) навык отвечает за следующие проверки: бег по льду, балансирование на натянутом канате или палубе корабля во время шторма;
        * self._stealth (int): Скрытность - (Ловкость) навык отвечает за следующие проверки: укрыться от врага, прокрасться мимо, незаметно подкрасться;
        * self._sleight_of_hand (int): Ловкость Рук - (Ловкость) навык отвечает за следующие проверки: жонглирование, ловкие трюки (подбросить что-то кому-то, стащить что-то из кармана/пояса);

        # ИНТЕЛЛЕКТ
        * self._analysis (int): Анализ - (Интеллект) навык отвечает за следующие проверки: поиск подсказок, выводы на основе подсказок, оценка окружения, поиск по подсказкам;
        * self._history (int): История - (Интеллект) навык отвечает за следующие проверки: знания исторических событий, легендарных личностей, древних королевств, былых спорах, недавних войнах и исчезнувших цивилизациях;
        * self._magic (int): Магия - (Интеллект) навык отвечает за следующие проверки: знания заклинаний, магических предметов, мистических символов, магических традиций;
        * self._nature (int): Природа - (Интеллект) навык отвечает за следующие проверки: знания о местности, о животных, о погоде и естественных циклах;
        * self._religion (int): Религия - (Интеллект) навык отвечает за следующие проверки: знания о божествах, ритуалах и молитвах, религиозных иерархиях, священных символах и практиках такных культов;;

        # МУДРОСТЬ
        * self._animal_care (int): Уход за животными - (Мудрость) навык отвечает за следующие проверки: возможность успокоить одомашненное животное, удержать скакуна от паники, почувствовать намерения животного;
        * self._insight (int): Проницательность - (Мудрость) навык отвечает за следующие проверки: определение истинных намерений существа, распознавание лжи, предсказание следующего шага;
        * self._medicine (int): Медицина - (Мудрость) навык отвечает за следующие проверки: лечение ран и болезней, стабилизация умирающего спутника, диагностирование болезней, определение причины смерти;;
        * self._perception (int): Внимательность - (Мудрость) навык отвечает за следующие проверки: возможность увидеть/услышать/унюхать/ощутить чьё-либо присутствие, готовность к новым событиям и остроту чувств;
        * self._survival (int): Выживание - (Мудрость) навык отвечает за следующие проверки: выслеживание врагов, охота на дичь, нахождение пути, определение опасности поблизости, предсказание погоды, избегание природных опасностей;

        # ХАРИЗМА
        * self._deception (int): Обман - (Харизма) навык отвечает за следующие проверки: способность утаить правду (речами или действиями), ложь, введение в заблуждение;
        * self._intimidation (int): Запугивание - (Харизма) навык отвечает за следующие проверки: угрозы, враждебные действия и физическое насилие;
        * self._performance (int): Выступление - (Харизма) навык отвечает за следующие проверки: удовлетворение публики музыкой, танцем, актёрской игрой, рассказом и т.д.;
        * self._persuasion (int): Убеждение - (Харизма) навык отвечает за следующие проверки: влияние на других тактично, с уважением и добродушием;

    Properties:
        * athletics - Геттер, отвечающий за получение значения навыка Атлетики;
        * acrobatics - Геттер, отвечающий за получение значения навыка Акробатика;
        * stealth - Геттер, отвечающий за получение значения навыка Скрытность;
        * sleight_of_hand - Геттер, отвечающий за получение значения навыка Ловкость Рук;
        * analysis - Геттер, отвечающий за получение значения навыка Анализ;
        * history - Геттер, отвечающий за получение значения навыка История;
        * magic - Геттер, отвечающий за получение значения навыка Магия;
        * nature - Геттер, отвечающий за получение значения навыка Природа;
        * religion - Геттер, отвечающий за получение значения навыка Религия;
        * animal_care - Геттер, отвечающий за получение значения навыка Забота о Животных;
        * insight - Геттер, отвечающий за получение значения навыка Проницательность;
        * medicine - Геттер, отвечающий за получение значения навыка Медицина;
        * perception - Геттер, отвечающий за получение значения навыка Восприятие;
        * survival - Геттер, отвечающий за получение значения навыка Выживание;
        * deception - Геттер, отвечающий за получение значения навыка Обман;
        * intimidation - Геттер, отвечающий за получение значения навыка Запугивание;
        * performance - Геттер, отвечающий за получение значения навыка Выступление;
        * persuasion - Геттер, отвечающий за получение значения навыка Убеждение;

    Raises:
        * TypeError: Некорректный тип данных;

    Methods:
        * calc_abilitie_value - Метод принимает на вход название способности и рассчитывает значение с учётом владения и бонуса мастерства.
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
            class_modifiers: BasicModifiers,
            class_proficiency_bonus: BasicProficiencyBonus,
            class_abilities_posessions: BasicAbilitiesPosessions
    ) -> None:
        for value, expected_type in zip(
                (class_modifiers, class_proficiency_bonus, class_abilities_posessions),
                (BasicModifiers, BasicProficiencyBonus, BasicAbilitiesPosessions),
        ):
            Check.value_type(
                value=value,
                expected_type=expected_type
            )

        self._class_modifiers: BasicModifiers = class_modifiers
        self._class_proficiency_bonus: BasicProficiencyBonus = class_proficiency_bonus
        self._class_abilities_posessions: BasicAbilitiesPosessions = class_abilities_posessions

        # СИЛА
        self._athletics: int = 0

        # ЛОВКОСТЬ
        self._acrobatics: int = 0
        self._stealth: int = 0
        self._sleight_of_hands: int = 0

        # ИНТЕЛЛЕКТ
        self._analysis: int = 0
        self._history: int = 0
        self._magic: int = 0
        self._nature: int = 0
        self._religion: int = 0

        # МУДРОСТЬ
        self._animal_care: int = 0
        self._insight: int = 0
        self._medicine: int = 0
        self._perception: int = 0
        self._survival: int = 0

        # ХАРИЗМА
        self._deception: int = 0
        self._intimidation: int = 0
        self._performance: int = 0
        self._persuasion: int = 0

        self.calculate_abilitie_value()



    # ##################################################
    # 5. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    @property
    def athletics(self) -> int:
        Check.value_type(value=self._athletics, expected_type=int)
        return self._athletics

    @property
    def acrobatics(self) -> int:
        Check.value_type(value=self._acrobatics, expected_type=int)
        return self._acrobatics

    @property
    def stealth(self) -> int:
        Check.value_type(value=self._stealth, expected_type=int)
        return self._stealth

    @property
    def sleight_of_hands(self) -> int:
        Check.value_type(value=self._sleight_of_hands, expected_type=int)
        return self._sleight_of_hands

    @property
    def analysis(self) -> int:
        Check.value_type(value=self._analysis, expected_type=int)
        return self._analysis

    @property
    def history(self) -> int:
        Check.value_type(value=self._history, expected_type=int)
        return self._history

    @property
    def magic(self) -> int:
        Check.value_type(value=self._magic, expected_type=int)
        return self._magic

    @property
    def nature(self) -> int:
        Check.value_type(value=self._nature, expected_type=int)
        return self._nature

    @property
    def religion(self) -> int:
        Check.value_type(value=self._religion, expected_type=int)
        return self._religion

    @property
    def animal_care(self) -> int:
        Check.value_type(value=self._animal_care, expected_type=int)
        return self._animal_care

    @property
    def insight(self) -> int:
        Check.value_type(value=self._insight, expected_type=int)
        return self._insight

    @property
    def medicine(self) -> int:
        Check.value_type(value=self._medicine, expected_type=int)
        return self._medicine

    @property
    def perception(self) -> int:
        Check.value_type(value=self._perception, expected_type=int)
        return self._perception

    @property
    def survival(self) -> int:
        Check.value_type(value=self._survival, expected_type=int)
        return self._survival

    @property
    def deception(self) -> int:
        Check.value_type(value=self._deception, expected_type=int)
        return self._deception

    @property
    def intimidation(self) -> int:
        Check.value_type(value=self._intimidation, expected_type=int)
        return self._intimidation

    @property
    def performance(self) -> int:
        Check.value_type(value=self._performance, expected_type=int)
        return self._performance

    @property
    def persuasion(self) -> int:
        Check.value_type(value=self._persuasion, expected_type=int)
        return self._persuasion


    # ##################################################
    # 6. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    def calculate_abilitie_value(self) -> None:
        """
        Notes:
            Метод принимает на вход название способности и рассчитывает значение с учётом владения и бонуса мастерства.

        Args:
            abilitie (str): Название способности.

        Returns:
            int: Значение способности.
        """


        self._acrobatics = (
            self._class_modifiers.dexterity + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.acrobatics
            else self._class_modifiers.dexterity
        )

        self._analysis = (
            self._class_modifiers.intelligence + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.analysis
            else self._class_modifiers.intelligence
        )
        self._animal_care = (
            self._class_modifiers.wisdom + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.animal_care
            else self._class_modifiers.wisdom
        )

        self._athletics = (
            self._class_modifiers.strength + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.athletics
            else self._class_modifiers.strength
        )

        self._deception = (
            self._class_modifiers.charisma + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.deception
            else self._class_modifiers.charisma
        )

        self._history = (
            self._class_modifiers.intelligence + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.history
            else self._class_modifiers.intelligence
        )

        self._insight = (
            self._class_modifiers.intelligence + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.insight
            else self._class_modifiers.intelligence
        )

        self._intimidation = (
            self._class_modifiers.charisma + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.intimidation
            else self._class_modifiers.charisma
        )

        self._magic = (
            self._class_modifiers.intelligence + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.magic
            else self._class_modifiers.intelligence
        )

        self._medicine = (
            self._class_modifiers.wisdom + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.medicine
            else self._class_modifiers.wisdom
        )

        self._nature = (
            self._class_modifiers.intelligence + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.nature
            else self._class_modifiers.intelligence
        )

        self._perception = (
            self._class_modifiers.wisdom + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.perception
            else self._class_modifiers.wisdom
        )

        self._performance = (
            self._class_modifiers.charisma + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.performance
            else self._class_modifiers.charisma
        )

        self._persuasion = (
            self._class_modifiers.charisma + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.persuasion
            else self._class_modifiers.charisma
        )

        self._religion = (
            self._class_modifiers.intelligence + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.religion
            else self._class_modifiers.intelligence
        )

        self._sleight_of_hands = (
            self._class_modifiers.dexterity + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.sleight_of_hands
            else self._class_modifiers.dexterity
        )

        self._stealth = (
            self._class_modifiers.dexterity + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.stealth
            else self._class_modifiers.dexterity
        )

        self._survival = (
            self._class_modifiers.wisdom + self._class_proficiency_bonus.proficiency_bonus
            if self._class_abilities_posessions.survival
            else self._class_modifiers.wisdom
        )
