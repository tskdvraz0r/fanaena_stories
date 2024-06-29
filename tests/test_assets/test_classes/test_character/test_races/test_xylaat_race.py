# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.xylaat_race import BasicRace

from fixtures.assets.classes.characters.races.fixture_xylaat_race import fixture_xylaat_race


# Костыль(?), чтобы избежать ошибки "Доступ к испорту dices не производится";
xylaat_race = fixture_xylaat_race

@pytest.mark.usefixtures("xylaat_race")
class TestBasicRace:

    def test_init_xylaat_race(
            self,
            xylaat_race: BasicRace
    ) -> None:
        Check.value_type(
            value=xylaat_race,
            expected_type=BasicRace
        )

    def test_xylaat_race_characteristic_modifiers_types(
            self,
            xylaat_race: BasicRace
    ) -> None:
        for characteristic in (
            xylaat_race.strength,
            xylaat_race.dexterity,
            xylaat_race.endurance,
            xylaat_race.intelligence,
            xylaat_race.wisdom,
            xylaat_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_xylaat_race_characteristic_modifiers_value(
            self,
            xylaat_race: BasicRace
    ) -> None:
        assert xylaat_race.strength == 0
        assert xylaat_race.dexterity == 2
        assert xylaat_race.endurance == 1
        assert xylaat_race.intelligence == 1
        assert xylaat_race.wisdom == 2
        assert xylaat_race.charisma == 0
