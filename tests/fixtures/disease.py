"""Define fixtures for "Disease"."""
import pytest


@pytest.fixture()
def fixture_current():
    """Return a /forecast/current/cold/<ZIP> response."""
    return {
        "ForecastDate": "2019-04-07T00:00:00-04:00",
        "Location": {
            "City": "DENVER",
            "DisplayLocation": "Denver, CO",
            "State": "CO",
            "ZIP": "80238",
            "periods": [
                {
                    "Idx": "6.8",
                    "Index": 6.8,
                    "Period": "2019-04-06T00:00:00",
                    "Triggers": [
                        {
                            "Description": "Influenza",
                            "Idx": "3.1",
                            "Index": 3.1,
                            "Name": "Flu"
                        },
                        {
                            "Description": "High Fever",
                            "Idx": "6.2",
                            "Index": 6.2,
                            "Name": "Fever"
                        },
                        {
                            "Description": "Strep & Sore throat",
                            "Idx": "5.2",
                            "Index": 5.2,
                            "Name": "Strep"
                        },
                        {
                            "Description": "Cough",
                            "Idx": "7.8",
                            "Index": 7.8,
                            "Name": "Cough"
                        }
                    ],
                    "Type": "Yesterday"
                },
                {
                    "Idx": "6.7",
                    "Index": 6.7,
                    "Period": "2019-04-07T03:52:58",
                    "Triggers": [
                        {
                            "Description": "Influenza",
                            "Idx": "3.1",
                            "Index": 3.1,
                            "Name": "Flu"
                        },
                        {
                            "Description": "High Fever",
                            "Idx": "5.9",
                            "Index": 5.9,
                            "Name": "Fever"
                        },
                        {
                            "Description": "Strep & Sore throat",
                            "Idx": "5.1",
                            "Index": 5.1,
                            "Name": "Strep"
                        },
                        {
                            "Description": "Cough",
                            "Idx": "7.7",
                            "Index": 7.7,
                            "Name": "Cough"
                        }
                    ],
                    "Type": "Today"
                }
            ]
        },
        "Type": "cold"
    }

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


@pytest.fixture()
def fixture_historic():
    """Return a /forecast/historic/cold/<ZIP> response."""
    return {
        "ForecastDate": "2019-04-07T00:00:00-04:00",
        "Location": {
            "City": "DENVER",
            "DisplayLocation": "Denver, CO",
            "State": "CO",
            "ZIP": "80238",
            "periods": [
                {
                    "Idx": "10.3",
                    "Index": 10.3,
                    "Period": "2019-03-08T00:00:00"
                },
                {
                    "Idx": "10.1",
                    "Index": 10.1,
                    "Period": "2019-03-09T00:00:00"
                },
                {
                    "Idx": "9.7",
                    "Index": 9.7,
                    "Period": "2019-03-10T00:00:00"
                },
                {
                    "Idx": "10.5",
                    "Index": 10.5,
                    "Period": "2019-03-11T00:00:00"
                },
                {
                    "Idx": "9.8",
                    "Index": 9.8,
                    "Period": "2019-03-14T00:00:00"
                },
                {
                    "Idx": "9.8",
                    "Index": 9.8,
                    "Period": "2019-03-15T00:00:00"
                },
                {
                    "Idx": "9.6",
                    "Index": 9.6,
                    "Period": "2019-03-16T00:00:00"
                },
                {
                    "Idx": "8.8",
                    "Index": 8.8,
                    "Period": "2019-03-17T00:00:00"
                },
                {
                    "Idx": "9.5",
                    "Index": 9.5,
                    "Period": "2019-03-18T00:00:00"
                },
                {
                    "Idx": "9.6",
                    "Index": 9.6,
                    "Period": "2019-03-19T00:00:00"
                },
                {
                    "Idx": "9.1",
                    "Index": 9.1,
                    "Period": "2019-03-20T00:00:00"
                },
                {
                    "Idx": "8.8",
                    "Index": 8.8,
                    "Period": "2019-03-21T00:00:00"
                },
                {
                    "Idx": "7.6",
                    "Index": 7.6,
                    "Period": "2019-03-22T00:00:00"
                },
                {
                    "Idx": "7.6",
                    "Index": 7.6,
                    "Period": "2019-03-23T00:00:00"
                },
                {
                    "Idx": "8.2",
                    "Index": 8.2,
                    "Period": "2019-03-24T00:00:00"
                },
                {
                    "Idx": "8.8",
                    "Index": 8.8,
                    "Period": "2019-03-25T00:00:00"
                },
                {
                    "Idx": "8.6",
                    "Index": 8.6,
                    "Period": "2019-03-26T00:00:00"
                },
                {
                    "Idx": "8.0",
                    "Index": 8.0,
                    "Period": "2019-03-27T00:00:00"
                },
                {
                    "Idx": "8.3",
                    "Index": 8.3,
                    "Period": "2019-03-28T00:00:00"
                },
                {
                    "Idx": "8.6",
                    "Index": 8.6,
                    "Period": "2019-03-29T00:00:00"
                },
                {
                    "Idx": "8.0",
                    "Index": 8.0,
                    "Period": "2019-04-02T00:00:00"
                },
                {
                    "Idx": "7.8",
                    "Index": 7.8,
                    "Period": "2019-04-03T00:00:00"
                },
                {
                    "Idx": "7.8",
                    "Index": 7.8,
                    "Period": "2019-04-04T00:00:00"
                },
                {
                    "Idx": "7.0",
                    "Index": 7.0,
                    "Period": "2019-04-05T00:00:00"
                },
                {
                    "Idx": "6.8",
                    "Index": 6.8,
                    "Period": "2019-04-06T00:00:00"
                },
                {
                    "Idx": "6.7",
                    "Index": 6.7,
                    "Period": "2019-04-07T03:52:58.203"
                }
            ]
        },
        "Type": "cold"
    }
