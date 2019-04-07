"""Define fixtures for "Asthma"."""
import pytest


@pytest.fixture()
def fixture_current():
    """Return a /forecast/current/asthma/<ZIP> response."""
    return {
        "Type": "asthma",
        "ForecastDate": "2018-10-29T00:00:00-04:00",
        "Location": {
            "ZIP": "80238",
            "City": "DENVER",
            "State": "CO",
            "periods": [{
                "Triggers": [{
                    "LGID": 1,
                    "Name": "OZONE",
                    "PPM": 42,
                    "Description": "Ozone (O3) is a odorless, colorless ...."
                }, {
                    "LGID": 1,
                    "Name": "PM2.5",
                    "PPM": 30,
                    "Description": "Fine particles (PM2.5) are 2.5 ..."
                }, {
                    "LGID": 1,
                    "Name": "PM10",
                    "PPM": 19,
                    "Description": "Coarse dust particles (PM10) are 2.5 ..."
                }],
                "Period": "0001-01-01T00:00:00",
                "Type": "Yesterday",
                "Index": 4.1,
                "Idx": "4.1"
            }, {
                "Triggers": [{
                    "LGID": 3,
                    "Name": "PM2.5",
                    "PPM": 105,
                    "Description": "Fine particles (PM2.5) are 2.5 ..."
                }, {
                    "LGID": 2,
                    "Name": "PM10",
                    "PPM": 65,
                    "Description": "Coarse dust particles (PM10) are 2.5 ..."
                }, {
                    "LGID": 1,
                    "Name": "OZONE",
                    "PPM": 42,
                    "Description": "Ozone (O3) is a odorless, colorless ..."
                }],
                "Period": "0001-01-01T00:00:00",
                "Type": "Today",
                "Index": 4.5,
                "Idx": "4.5"
            }, {
                "Triggers": [],
                "Period": "0001-01-01T00:00:00",
                "Type": "Tomorrow",
                "Index": 4.6,
                "Idx": "4.6"
            }],
            "DisplayLocation":
                "Denver, CO"
        }
    }


@pytest.fixture()
def fixture_extended():
    """Return a /forecast/extended/asthma/<ZIP> response."""
    return {
        "Type": "asthma",
        "ForecastDate": "2018-10-28T00:00:00-04:00",
        "Location": {
            "ZIP": "73344",
            "City": "AUSTIN",
            "State": "TX",
            "periods": [{
                "Period": "2018-10-28T05:45:01.45",
                "Index": 4.5,
                "Idx": "4.5"
            }, {
                "Period": "2018-10-29T05:45:01.45",
                "Index": 4.7,
                "Idx": "4.7"
            }, {
                "Period": "2018-10-30T05:45:01.45",
                "Index": 5.0,
                "Idx": "5.0"
            }, {
                "Period": "2018-10-31T05:45:01.45",
                "Index": 5.2,
                "Idx": "5.2"
            }, {
                "Period": "2018-11-01T05:45:01.45",
                "Index": 5.5,
                "Idx": "5.5"
            }],
            "DisplayLocation":
                "Austin, TX"
        }
    }


@pytest.fixture()
def fixture_historic():
    """Return a /forecast/historic/asthma/<ZIP> response."""
    return {
        "Type": "asthma",
        "ForecastDate": "2018-10-28T00:00:00-04:00",
        "Location": {
            "ZIP": "73344",
            "City": "AUSTIN",
            "State": "TX",
            "periods": [{
                "Period": "2018-09-29T05:45:00.123",
                "Index": 5.5,
                "Idx": "5.5"
            }, {
                "Period": "2018-09-30T05:45:00.157",
                "Index": 6.3,
                "Idx": "6.3"
            }, {
                "Period": "2018-10-01T05:44:59.45",
                "Index": 5.9,
                "Idx": "5.9"
            }, {
                "Period": "2018-10-02T05:44:59.677",
                "Index": 6.1,
                "Idx": "6.1"
            }, {
                "Period": "2018-10-03T05:45:00.237",
                "Index": 6.1,
                "Idx": "6.1"
            }, {
                "Period": "2018-10-04T05:44:59.117",
                "Index": 6.1,
                "Idx": "6.1"
            }, {
                "Period": "2018-10-05T05:45:00.223",
                "Index": 5.9,
                "Idx": "5.9"
            }, {
                "Period": "2018-10-05T05:45:00.223",
                "Index": 5.9,
                "Idx": "5.9"
            }, {
                "Period": "2018-10-07T05:45:00.97",
                "Index": 5.0,
                "Idx": "5.0"
            }, {
                "Period": "2018-10-08T05:45:00.577",
                "Index": 3.7,
                "Idx": "3.7"
            }, {
                "Period": "2018-10-09T05:45:04.743",
                "Index": 3.4,
                "Idx": "3.4"
            }, {
                "Period": "2018-10-10T05:44:59.227",
                "Index": 5.4,
                "Idx": "5.4"
            }, {
                "Period": "2018-10-11T05:45:00.62",
                "Index": 5.7,
                "Idx": "5.7"
            }, {
                "Period": "2018-10-12T05:45:00.723",
                "Index": 5.2,
                "Idx": "5.2"
            }, {
                "Period": "2018-10-13T05:44:59.003",
                "Index": 4.5,
                "Idx": "4.5"
            }, {
                "Period": "2018-10-14T05:44:59.233",
                "Index": 3.8,
                "Idx": "3.8"
            }, {
                "Period": "2018-10-15T05:44:58.457",
                "Index": 3.1,
                "Idx": "3.1"
            }, {
                "Period": "2018-10-16T05:44:58.73",
                "Index": 2.9,
                "Idx": "2.9"
            }, {
                "Period": "2018-10-17T05:44:58.423",
                "Index": 3.9,
                "Idx": "3.9"
            }, {
                "Period": "2018-10-18T05:44:59.05",
                "Index": 3.7,
                "Idx": "3.7"
            }, {
                "Period": "2018-10-19T05:45:00.21",
                "Index": 2.9,
                "Idx": "2.9"
            }, {
                "Period": "2018-10-20T05:45:01.003",
                "Index": 3.4,
                "Idx": "3.4"
            }, {
                "Period": "2018-10-21T05:45:03.393",
                "Index": 5.4,
                "Idx": "5.4"
            }, {
                "Period": "2018-10-22T05:44:58.487",
                "Index": 4.1,
                "Idx": "4.1"
            }, {
                "Period": "2018-10-23T05:44:58.63",
                "Index": 3.1,
                "Idx": "3.1"
            }, {
                "Period": "2018-10-24T05:45:12.88",
                "Index": 2.9,
                "Idx": "2.9"
            }, {
                "Period": "2018-10-25T05:44:59.347",
                "Index": 4.5,
                "Idx": "4.5"
            }, {
                "Period": "2018-10-26T05:44:58.96",
                "Index": 4.8,
                "Idx": "4.8"
            }, {
                "Period": "2018-10-26T05:44:58.96",
                "Index": 4.8,
                "Idx": "4.8"
            }, {
                "Period": "2018-10-28T05:45:01.45",
                "Index": 4.5,
                "Idx": "4.5"
            }],
            "DisplayLocation": "Austin, TX"
        }
    }
