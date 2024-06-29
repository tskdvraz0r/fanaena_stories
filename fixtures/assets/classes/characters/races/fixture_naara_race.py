import pytest

from assets.classes.characters.races.basic_race import BasicRace
from assets.classes.characters.races.naara_race import NaaraRace

@pytest.fixture
def fixture_naara_race() -> BasicRace:
    naara_race: BasicRace = NaaraRace()

    return naara_race
