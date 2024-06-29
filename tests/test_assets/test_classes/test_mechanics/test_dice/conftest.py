import pytest

from assets.classes.mechanics.dice.dice import Dice


@pytest.fixture
def fixture_dices() -> list[Dice]:
    dices: list[Dice] = [
        Dice(d=2),
        Dice(d=4),
        Dice(d=6),
        Dice(d=8),
        Dice(d=10),
        Dice(d=12),
        Dice(d=20),
        Dice(d=100),
        Dice(d=1000)
    ]

    return dices
