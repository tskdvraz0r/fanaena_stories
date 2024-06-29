# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.naara_race import BasicRace


@pytest.mark.usefixtures("fixture_naara_race")
class TestBasicRace:

    def test_init_fixture_naara_race(
            self,
            fixture_naara_race: BasicRace
    ) -> None:
        Check.value_type(
            value=fixture_naara_race,
            expected_type=BasicRace
        )

    def test_fixture_naara_race_characteristic_modifiers_types(
            self,
            fixture_naara_race: BasicRace
    ) -> None:
        for characteristic in (
            fixture_naara_race.strength,
            fixture_naara_race.dexterity,
            fixture_naara_race.endurance,
            fixture_naara_race.intelligence,
            fixture_naara_race.wisdom,
            fixture_naara_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_fixture_naara_race_characteristic_modifiers_value(
            self,
            fixture_naara_race: BasicRace
    ) -> None:
        assert fixture_naara_race.strength == 3
        assert fixture_naara_race.dexterity == 0
        assert fixture_naara_race.endurance == 2
        assert fixture_naara_race.intelligence == 0
        assert fixture_naara_race.wisdom == 1
        assert fixture_naara_race.charisma == 0
