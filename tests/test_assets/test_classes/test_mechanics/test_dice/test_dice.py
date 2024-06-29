# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from assets.classes.mechanics.dice.dice import Dice

from packages.engine.data_validation.check import Check


@pytest.mark.usefixtures("fixture_dices")
class TestDice:

    def test_init_dices(
            self,
            fixture_dices: list[Dice]
    ) -> None:
        for dice in fixture_dices:
            Check.value_type(
                value=dice,
                expected_type=Dice
            )

    def test_create_available_dices(
            self,
            fixture_dices: list[Dice]
    ) -> None:
        for dice in fixture_dices:
            Check.value_is_available(
                value=dice.d,
                available_values=Dice.get_available_dices()
            )

    def test_roll_dices(
            self,
            fixture_dices: list[Dice]
    ) -> None:
        for dice in fixture_dices:
            Check.value_is_available(
                value=dice.roll(),
                available_values=range(1, dice.d + 1)
            )
