# TASK 1: Реализовать класс *"Check"*;
## 1. Описание;
Реализовать класс *"Check"*, отвечающий за проверку корректности входных и выходных данных.


## 1. Атрибуты класса;
*Атрибуты* класса не предусмотрены.


## 2. Свойства класса;
*Свойства* класса не предусмотрены.


## 3. Методы класса;
Класс должен иметь следующие *методы*:
```python 3.13
def value_type(
        value: typing.Any,
        expected_type: typing.Any
) -> None:
    """
    Notes:
        Метод принимает на вход проверяемое значение и ожидаемый тип данных.
        Производит проверку: соответствует ли тип данных переданного значения
        к ожидаемому.

    Attributes:
        value (typing.Any): проверяемое значение;
        expected_type (typing.Any): ожидаемый тип данных.

    Raises:
        TypeError: Некорректный тип данных.
    """
```

```python 3.13
def value_is_available(
        value: tiping.Any,
        available_values: typing.Any
) -> None:
    """
    Notes:
        Метод принимает на вход проверяемое значение и любой
        массив/кортеж/множество с доступными значениями. Производит проверку:
        является ли переданное значение доступным к использованию.

    Attributes:
        value (typing.Any): проверяемое значение;
        available_values (typing.Any): любой массив/кортеж/множество с
        доступными значениями.

    Raises:
        ValueError: недоступное значение.
    """
```


## 4. Инициализация экземпляра класса;
*Инициализация* экземпляра класса не предусмотрена.


## 5. Атрибуты экземпляра класса;
*Атрибуты* экземпляра класса не предусмотрены.


## 6. Свойства экземпляра класса;
*Свойства* экземпляра класса не предусмотрены.


## 7. Методы экземпляра класса;
*Методы* экземпляра класса не предусмотрены.
