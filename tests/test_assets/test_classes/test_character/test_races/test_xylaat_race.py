# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.xylaat_race import BasicRace


@pytest.mark.usefixtures("fixture_xylaat_race")
class TestBasicRace:

    def test_init_fixture_xylaat_race(
            self,
            fixture_xylaat_race: BasicRace
    ) -> None:
        Check.value_type(
            value=fixture_xylaat_race,
            expected_type=BasicRace
        )

    def test_fixture_xylaat_race_characteristic_modifiers_types(
            self,
            fixture_xylaat_race: BasicRace
    ) -> None:
        for characteristic in (
            fixture_xylaat_race.strength,
            fixture_xylaat_race.dexterity,
            fixture_xylaat_race.endurance,
            fixture_xylaat_race.intelligence,
            fixture_xylaat_race.wisdom,
            fixture_xylaat_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_fixture_xylaat_race_characteristic_modifiers_value(
            self,
            fixture_xylaat_race: BasicRace
    ) -> None:
        assert fixture_xylaat_race.strength == 0
        assert fixture_xylaat_race.dexterity == 2
        assert fixture_xylaat_race.endurance == 1
        assert fixture_xylaat_race.intelligence == 1
        assert fixture_xylaat_race.wisdom == 2
        assert fixture_xylaat_race.charisma == 0
