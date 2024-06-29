import pytest

from assets.classes.characters.races.basic_race import BasicRace
from assets.classes.characters.races.xylaat_race import XylaatRace

@pytest.fixture
def fixture_xylaat_race() -> BasicRace:
    xylaat_race: BasicRace = XylaatRace()

    return xylaat_race
