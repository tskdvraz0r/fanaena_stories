# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.zenhaas_race import BasicRace

from fixtures.assets.classes.characters.races.fixture_zenhaas_race import fixture_zenhaas_race


# Костыль(?), чтобы избежать ошибки "Доступ к испорту dices не производится";
zenhaas_race = fixture_zenhaas_race

@pytest.mark.usefixtures("zenhaas_race")
class TestHumanRace:

    def test_init_zenhaas_race(
            self,
            zenhaas_race: BasicRace
    ) -> None:
        Check.value_type(
            value=zenhaas_race,
            expected_type=BasicRace
        )

    def test_zenhaas_race_characteristic_modifiers_types(
            self,
            zenhaas_race: BasicRace
    ) -> None:
        for characteristic in (
            zenhaas_race.strength,
            zenhaas_race.dexterity,
            zenhaas_race.endurance,
            zenhaas_race.intelligence,
            zenhaas_race.wisdom,
            zenhaas_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_zenhaas_race_characteristic_modifiers_value(
            self,
            zenhaas_race: BasicRace
    ) -> None:
        assert zenhaas_race.strength == 2
        assert zenhaas_race.dexterity == 0
        assert zenhaas_race.endurance == 2
        assert zenhaas_race.intelligence == 0
        assert zenhaas_race.wisdom == 2
        assert zenhaas_race.charisma == 0
