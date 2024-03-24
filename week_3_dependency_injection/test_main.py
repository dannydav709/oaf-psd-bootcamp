from main import DataSourceHandler, APICallingService
import unittest
from unittest.mock import MagicMock


def mock_data_service():
    mock_service = MagicMock()
    mock_service.fetch_data.return_value = {"temperature": 20, "weather": "sunny"}
    return mock_service


def test_DataSourceHandler():
    handler = DataSourceHandler(mock_data_service())
    assert handler.handle_data() is not None


def test_APICallingService():
    api = APICallingService("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m")
    assert api.fetch_data() is not None
    # test_DataSourceHandler()