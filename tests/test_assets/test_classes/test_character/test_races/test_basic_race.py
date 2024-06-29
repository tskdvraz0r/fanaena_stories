# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.basic_race import BasicRace

from fixtures.assets.classes.characters.races.fixture_basic_race import fixture_basic_race


# Костыль(?), чтобы избежать ошибки "Доступ к испорту dices не производится";
basic_race = fixture_basic_race

@pytest.mark.usefixtures("basic_race")
class TestBasicRace:

    def test_init_basic_race(
            self,
            basic_race: BasicRace
    ) -> None:
        Check.value_type(
            value=basic_race,
            expected_type=BasicRace
        )

    def test_basic_race_characteristic_modifiers_types(
            self,
            basic_race: BasicRace
    ) -> None:
        for characteristic in (
            basic_race.strength,
            basic_race.dexterity,
            basic_race.endurance,
            basic_race.intelligence,
            basic_race.wisdom,
            basic_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_basic_race_characteristic_modifiers_value(
            self,
            basic_race: BasicRace
    ) -> None:
        assert basic_race.strength == 0
        assert basic_race.dexterity == 0
        assert basic_race.endurance == 0
        assert basic_race.intelligence == 0
        assert basic_race.wisdom == 0
        assert basic_race.charisma == 0
