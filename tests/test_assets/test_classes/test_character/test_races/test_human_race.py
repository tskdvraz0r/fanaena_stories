# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.human_race import BasicRace

from fixtures.assets.classes.characters.races.fixture_human_race import fixture_human_race


# Костыль(?), чтобы избежать ошибки "Доступ к испорту dices не производится";
human_race = fixture_human_race

@pytest.mark.usefixtures("human_race")
class TestHumanRace:

    def test_init_human_race(
            self,
            human_race: BasicRace
    ) -> None:
        Check.value_type(
            value=human_race,
            expected_type=BasicRace
        )

    def test_human_race_characteristic_modifiers_types(
            self,
            human_race: BasicRace
    ) -> None:
        for characteristic in (
            human_race.strength,
            human_race.dexterity,
            human_race.endurance,
            human_race.intelligence,
            human_race.wisdom,
            human_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_human_race_characteristic_modifiers_value(
            self,
            human_race: BasicRace
    ) -> None:
        assert human_race.strength == 1
        assert human_race.dexterity == 1
        assert human_race.endurance == 1
        assert human_race.intelligence == 1
        assert human_race.wisdom == 1
        assert human_race.charisma == 1
