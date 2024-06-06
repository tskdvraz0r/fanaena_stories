# TASK 2: Реализовать класс **"Dice"**;
## 1. Описание;
Реализовать класс **"Dice"**, отвечающий за создание экземпляра игрового кубика и методов взаимодействия с ним.


## 1. Атрибуты класса;
Класс должен иметь следующие *атрибуты*:
* _available_dices (set[int]): множество значений, доступных для инициализации класса. Принимает следующие значения: 2, 4, 6, 8, 10, 12, 20, 100, 1000.


## 2. Свойства класса;
*Свойства* класса не предусмотрены.


## 3. Методы класса;
*Методы* класса не предусмотрены.


## 4. Инициализация экземпляра класса;
При инициализации экземпляра класс должен принимать следующие *аргументы*:
* d (int): количество граней игрового кубика.


## 5. Атрибуты экземпляра класса;
Экземпляр класса должен иметь следующие *атрибуты*:
* _d (int): количество граней игрового кубика.


## 6. Свойства экземпляра класса;
Экземпляр класса должен иметь следующие *свойства*:
```python 3.13
def d(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения количества граней кубика.

    Returns:
        (int): количество граней игрового кубика.
    """
```


## 7. Методы экземпляра класса;
*Методы* экземпляра класса не предусмотрены.
Экземпляр класса должен иметь следующие *методы*:
```python 3.13
def roll(self) -> int:
    """
    Notes:
        Метод отвечающий за симуляцию броска игрового кубига. Генерирует псевдослучайное число в доступном диапазоне, зависящем от количества граней кубика.

    Returns:
        (int): псевдослучайно число.
    """
```