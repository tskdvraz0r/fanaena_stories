# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.human_race import BasicRace


@pytest.mark.usefixtures("fixture_human_race")
class TestHumanRace:

    def test_init_fixture_human_race(
            self,
            fixture_human_race: BasicRace
    ) -> None:
        Check.value_type(
            value=fixture_human_race,
            expected_type=BasicRace
        )

    def test_fixture_human_race_characteristic_modifiers_types(
            self,
            fixture_human_race: BasicRace
    ) -> None:
        for characteristic in (
            fixture_human_race.strength,
            fixture_human_race.dexterity,
            fixture_human_race.endurance,
            fixture_human_race.intelligence,
            fixture_human_race.wisdom,
            fixture_human_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_fixture_human_race_characteristic_modifiers_value(
            self,
            fixture_human_race: BasicRace
    ) -> None:
        assert fixture_human_race.strength == 1
        assert fixture_human_race.dexterity == 1
        assert fixture_human_race.endurance == 1
        assert fixture_human_race.intelligence == 1
        assert fixture_human_race.wisdom == 1
        assert fixture_human_race.charisma == 1
