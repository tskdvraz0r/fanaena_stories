# ##################################################
# ИМПОРТ
# ##################################################

# Стандартные библиотеки
import typing

# Сторонние библиотеки
...

# Проектные библиотеки
...

# ##################################################
# КЛАССЫ
# ##################################################

class Check:
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

    @staticmethod
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

        if isinstance(value, expected_type):
            raise TypeError("Некорректный тип данных;")


    @staticmethod
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

        if value not in available_values:
            raise ValueError("Некорректное значение;")


    # ##################################################
    # 4. ИНИЦИАЛИЗАЦИЯ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 5. АТРИБУТЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 6. СВОЙСТВА ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...


    # ##################################################
    # 7. МЕТОДЫ ЭКЗЕМПЛЯРА КЛАССА
    # ##################################################
    ...
