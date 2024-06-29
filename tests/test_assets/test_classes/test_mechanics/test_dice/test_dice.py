# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from assets.classes.mechanics.dice.dice import Dice

from fixtures.assets.classes.mechanics.dice.fixture_dice import fixture_dices

from packages.engine.data_validation.check import Check


# Костыль(?), чтобы избежать ошибки "Доступ к испорту dices не производится";
dices = fixture_dices


@pytest.mark.usefixtures("dices")
class TestDice:

    def test_init_dices(
            self,
            dices: list[Dice]
    ) -> None:
        for dice in dices:
            Check.value_type(
                value=dice,
                expected_type=Dice
            )

    def test_create_available_dices(
            self,
            dices: list[Dice]
    ) -> None:
        for dice in dices:
            Check.value_is_available(
                value=dice.d,
                available_values=Dice.get_available_dices()
            )

    def test_roll_dices(
            self,
            dices: list[Dice]
    ) -> None:
        for dice in dices:
            Check.value_is_available(
                value=dice.roll(),
                available_values=range(1, dice.d + 1)
            )
