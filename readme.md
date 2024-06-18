# ИСТОРИИ ФАНАЭНЫ
## Версия: 0.17.9

## Описание:
Консольная (на данный момент) приключенческая RPG-игра. Частично заимствует механики DnD.


## Амбиции:
[TODO](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/todo.md)

## Обновления
### 19.06.2024
* 1. [FEAT-24] Реализован класс BasicProficiencyBonus;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/stats/proficiency_bonus/task_24_basic_proficiency_bonus.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/stats/proficiency_bonus/basic_proficiency_bonus.py)

* 2. [FEAT-16] Реализован класс BasicLevel;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/stats/level/task_16_basic_level.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/stats/level/basic_level.py)


### 11.06.2024
* 1. [REFACT] Полная переработка внутренней "архитектуры" проекта.


### 10.06.2024
* 1. [FEAT-9] Реализован класс HumanRace;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/races/task_9_human_race.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/races/human_race.py)

* 2. [FEAT-10] Реализован класс ZenhaasRace;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/races/task_10_zenhaas_race.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/races/zenhaas_race.py)

* 3. [FEAT-11] Реализован класс XylaatRace;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/races/task_11_xylaat_race.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/races/xylaat_race.py)

* 4. [FEAT-12] Реализован класс NaaraRace;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/races/task_12_naara_race.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/races/naara_race.py)

* 5. [FEAT-13] Реализован класс WarriorProfession;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/professions/task_13_warrior_profession.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/professions/warrior_profession.py)

* 6. [FEAT-14] Реализован класс RangerProfession;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/professions/task_14_ranger_profession.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/professions/ranger_profession.py)

* 7. [FEAT-15] Реализован класс WizzardProfession;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/characters/professions/task_15_wizzard_profession.md)
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/assets/classes/characters/professions/wizzard_profession.py)



### 07.06.2024
* 1. [FEAT-5] Реализован класс Characteristics;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/character/characteristics.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/character/characteristics.py)

* 2. [FEAT-6] Реализован класс Modifiers;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/character/modifiers.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/character/modifiers.py)

* 3. [FEAT-4] Реализован класс Profession;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/character/professions.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/character/professions.py)

* 4. [REFACT-6.1] Изменён метод инициализации экземпляра класса Modifiers;

* 5. [FEAT-7] Реализован класс HSMP (health/mana/stamina points);
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/character/hmsp.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/character/hmsp.py)

* 6. [FEAT-8] Реализован класс Character;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/character/characters.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/character/characters.py)

* 7. [REFACT-5.1] Изменён метод инициализации экземпляра класса Characteristics;


### 06.06.2024
* 1. [FEAT-2] Реализован класс Dice;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/mechanics/basic/dice.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/mechanics/basic/dice.py)

* 2. [FIX-1.2] Исправлена ошибка в методе value_type класса Check;

* 3. [REFACT-2.1] Добавлено новое значение (1000) для инициализации экземпляра класса Dice;

* 4. [FEAT-3] Реализован класс Race;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/character/races.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/character/races.py)


### 05.06.2024
* 1. [FEAT-1] Реализован класс Check;
[Документация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/docs/classes/engine/data_validation/check.md),
[Реализация](https://github.com/tskdvraz0r/fanaena_stories/blob/main/classes/engine/data_validation/check.py)

* 2. [FIX-1.1] Исправлены опечатки возбуждаемых исключений;
