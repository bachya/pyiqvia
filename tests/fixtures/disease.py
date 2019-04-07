"""Define fixtures for "Disease"."""
import pytest


@pytest.fixture()
def fixture_extended():
    """Return a /forecast/extended/cold/<ZIP> response."""
    return {
        "Type": "cold",
        "ForecastDate": "2018-06-12T00:00:00-04:00",
        "Location": {
            "ZIP": "80238",
            "City": "DENVER",
            "State": "CO",
            "periods": [{
                "Period": "2018-06-12T05:13:51.817",
                "Index": 2.4
            }, {
                "Period": "2018-06-13T05:13:51.817",
                "Index": 2.5
            }, {
                "Period": "2018-06-14T05:13:51.817",
                "Index": 2.5
            }, {
                "Period": "2018-06-15T05:13:51.817",
                "Index": 2.5
            }],
            "DisplayLocation": "Denver, CO"
        }
    }
