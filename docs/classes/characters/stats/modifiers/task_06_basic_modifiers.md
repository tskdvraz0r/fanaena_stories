# TASK 6: Реализовать класс **"BasicModifiers"**;
## 1. Описание;
Реализовать класс **"BasicModifiers"**, отвечающий за модификаторы характеристик.


## 1. Атрибуты класса;
*Атрибуты* класса не предусмотрены.


## 2. Свойства класса;
*Свойства* класса не предусмотрены.


## 3. Методы класса;
*Методы* класса не предусмотрены.


## 4. Инициализация экземпляра класса;
При инициализации экземпляра класс должен принимать следующие *аргументы*:
* class_characteristics (Characteristics): экземпляр класса Характеристик персонажа.


## 5. Атрибуты экземпляра класса;
Экземпляр класса должен иметь следующие *атрибуты*:
* _class_characteristics (Characteristics): экземпляр класса Характеристик персонажа.
* _strength: int - модификатор Силы;
* _dexterity: int - модификатор Ловкости;
* _endurance: int - модификатор Выносливости;
* _intelligence: int - модификатор Интеллекта;
* _wisdom: int - модификатор Мудрости;
* _charisma: int - модификатор Харизмы.

По умолчанию все модификаторы характеристик расчитываются по формуле:
```python3.13
characteristic = calc_modifier(characteristic=self._class_characteristics.характеристика)
```


## 6. Свойства экземпляра класса;
Экземпляр класса должен иметь следующие *свойства*:
```python 3.13
@property
def strength(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения модификатора Силы персонажа.
    """
    pass

@property
def dexterity(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения модификатора Ловкости персонажа.
    """
    pass

@property
def endurance(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения модификатора Телосложения персонажа.
    """
    pass

@property
def intelligence(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения модификатора Интеллекта персонажа.
    """
    pass

@property
def wisdom(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения модификатора Мудрости персонажа.
    """
    pass

@property
def charisma(self) -> int:
    """
    Notes:
        Геттер, отвечающий за получение значения модификатора Харизмы персонажа.
    """
    pass
```

## 7. Методы экземпляра класса;
Экземпляр класса должен иметь следующие *методы*:
```python 3.13
def calc_modifier(
        self,
        characteristic: int
) -> int:
    """
    Notes:
        Метод рассчитывает модификатор по формуле: math.floor((characteristic - 10) / 2).
    """
    pass

```