import pytest

from assets.classes.characters.races.basic_race import BasicRace
from assets.classes.characters.races.human_race import HumanRace
from assets.classes.characters.races.naara_race import NaaraRace
from assets.classes.characters.races.xylaat_race import XylaatRace
from assets.classes.characters.races.zenhaas_race import ZenhaasRace

@pytest.fixture
def fixture_basic_race() -> BasicRace:
    basic_race: BasicRace = BasicRace()

    return basic_race

@pytest.fixture
def fixture_human_race() -> BasicRace:
    human_race: BasicRace = HumanRace()

    return human_race

@pytest.fixture
def fixture_naara_race() -> BasicRace:
    naara_race: BasicRace = NaaraRace()

    return naara_race

@pytest.fixture
def fixture_xylaat_race() -> BasicRace:
    xylaat_race: BasicRace = XylaatRace()

    return xylaat_race

@pytest.fixture
def fixture_zenhaas_race() -> BasicRace:
    basic_zenhaas: BasicRace = ZenhaasRace()

    return basic_zenhaas
