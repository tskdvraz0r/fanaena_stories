# НАИМЕНОВАНИЕ: Истории Фанаэны
## ОПИСАНИЕ
Консольная (на данный момент) приключенческая RPG-игра. Частично заимствует механики DnD.

## ПЛАНЫ И АМБИЦИИ
* 1. Разные уровни сложности игры;
* 2. Вариативность создания персонажа: от пресетов и ручных настроек, до беспощадного рандома;
* 3. Создание локаций без применения процедурной генерации;
* 4. Создание квестов с интересными (или не очень) историями. Нелинейность прохождения (где это возможно);


## ОБНОВЛЕНИЯ
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
