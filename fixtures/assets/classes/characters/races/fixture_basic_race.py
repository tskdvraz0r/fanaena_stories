import pytest

from assets.classes.characters.races.basic_race import BasicRace

@pytest.fixture
def fixture_basic_race() -> BasicRace:
    basic_race: BasicRace = BasicRace()

    return basic_race
