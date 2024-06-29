import pytest

from assets.classes.characters.races.basic_race import BasicRace
from assets.classes.characters.races.zenhaas_race import ZenhaasRace

@pytest.fixture
def fixture_zenhaas_race() -> BasicRace:
    basic_zenhaas: BasicRace = ZenhaasRace()

    return basic_zenhaas
