import pytest
import kursy_walut



def test_pobierz_euro_z_mockiem(mocker):
    falszywe_dane = {
        "rates": [
            {"mid": 5.55}
        ]
    }

    mock_get = mocker.patch('kursy_walut.requests.get')

    mock_get.return_value.json.return_value = falszywe_dane
    wynik = kursy_walut.pobierz_euro()
    assert wynik == 5.55
