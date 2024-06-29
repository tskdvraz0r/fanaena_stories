import pytest

from assets.classes.characters.races.basic_race import BasicRace
from assets.classes.characters.races.human_race import HumanRace

@pytest.fixture
def fixture_human_race() -> BasicRace:
    human_race: BasicRace = HumanRace()

    return human_race
