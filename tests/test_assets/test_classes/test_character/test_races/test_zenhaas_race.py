# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.zenhaas_race import BasicRace


@pytest.mark.usefixtures("fixture_zenhaas_race")
class TestHumanRace:

    def test_init_fixture_zenhaas_race(
            self,
            fixture_zenhaas_race: BasicRace
    ) -> None:
        Check.value_type(
            value=fixture_zenhaas_race,
            expected_type=BasicRace
        )

    def test_fixture_zenhaas_race_characteristic_modifiers_types(
            self,
            fixture_zenhaas_race: BasicRace
    ) -> None:
        for characteristic in (
            fixture_zenhaas_race.strength,
            fixture_zenhaas_race.dexterity,
            fixture_zenhaas_race.endurance,
            fixture_zenhaas_race.intelligence,
            fixture_zenhaas_race.wisdom,
            fixture_zenhaas_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_fixture_zenhaas_race_characteristic_modifiers_value(
            self,
            fixture_zenhaas_race: BasicRace
    ) -> None:
        assert fixture_zenhaas_race.strength == 2
        assert fixture_zenhaas_race.dexterity == 0
        assert fixture_zenhaas_race.endurance == 2
        assert fixture_zenhaas_race.intelligence == 0
        assert fixture_zenhaas_race.wisdom == 2
        assert fixture_zenhaas_race.charisma == 0
