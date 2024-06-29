# Стандартные библиотеки
...

# Сторонние библиотеки
import pytest

# Проектные библиотеки
from packages.engine.data_validation.check import Check

from assets.classes.characters.races.naara_race import BasicRace

from fixtures.assets.classes.characters.races.fixture_naara_race import fixture_naara_race


# Костыль(?), чтобы избежать ошибки "Доступ к испорту dices не производится";
naara_race = fixture_naara_race

@pytest.mark.usefixtures("naara_race")
class TestBasicRace:

    def test_init_naara_race(
            self,
            naara_race: BasicRace
    ) -> None:
        Check.value_type(
            value=naara_race,
            expected_type=BasicRace
        )

    def test_naara_race_characteristic_modifiers_types(
            self,
            naara_race: BasicRace
    ) -> None:
        for characteristic in (
            naara_race.strength,
            naara_race.dexterity,
            naara_race.endurance,
            naara_race.intelligence,
            naara_race.wisdom,
            naara_race.charisma
        ):
            Check.value_type(
                value=characteristic,
                expected_type=int
            )

    def test_naara_race_characteristic_modifiers_value(
            self,
            naara_race: BasicRace
    ) -> None:
        assert naara_race.strength == 3
        assert naara_race.dexterity == 0
        assert naara_race.endurance == 2
        assert naara_race.intelligence == 0
        assert naara_race.wisdom == 1
        assert naara_race.charisma == 0
