from utils.download_osm_data import find_region_of_city, download_city_address
import pytest


@pytest.mark.parametrize("city, region", [
    ('Екатеринбург', 'Свердловская область'),
    ('Москва', 'Москва'),
    ('Агрыз', 'Татарстан'),
    ('Архангельск', 'Архангельская область'),
    ('Буй', 'Костромская область'),
    ('Волжск', 'Марий Эл'),
    ('Губкинский', 'Ямало-Ненецкий автономный округ'),
    ('Истра', 'Московская область'),
])
def test_findRegionOfCity(city, region):
    assert find_region_of_city(city) == region


@pytest.mark.parametrize("city", [
    ('екат'),
])
def test_fail_findRefionOfCity(city):
    with pytest.raises(ValueError):
        find_region_of_city(city)


def test_downloadAllAddr():
    assert len(download_city_address('Верхняя Салда')) != 0
