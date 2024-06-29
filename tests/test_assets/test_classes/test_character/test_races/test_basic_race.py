# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.basic_race import BasicRace


@pytest.mark.usefixtures("fixture_basic_race")
class TestBasicRace:

    def test_init_basic_race(
            self,
            fixture_basic_race: BasicRace
    ) -> None:
        Check.value_type(
            value=fixture_basic_race,
            expected_type=BasicRace
        )

    def test_basic_race_characteristic_modifiers_types(
            self,
            fixture_basic_race: BasicRace
    ) -> None:
        for characteristic in (
            fixture_basic_race.strength,
            fixture_basic_race.dexterity,
            fixture_basic_race.endurance,
            fixture_basic_race.intelligence,
            fixture_basic_race.wisdom,
            fixture_basic_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_basic_race_characteristic_modifiers_value(
            self,
            fixture_basic_race: BasicRace
    ) -> None:
        assert fixture_basic_race.strength == 0
        assert fixture_basic_race.dexterity == 0
        assert fixture_basic_race.endurance == 0
        assert fixture_basic_race.intelligence == 0
        assert fixture_basic_race.wisdom == 0
        assert fixture_basic_race.charisma == 0
