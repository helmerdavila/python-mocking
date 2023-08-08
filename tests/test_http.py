from unittest.mock import patch
from python_mocking import call_single_endpoint


@patch("requests.get")
def test_call_single_endpoint_mock(mocked_requests_get):
    call_single_endpoint()
    assert mocked_requests_get.called_once


class TestRequests:
    @patch("requests.get")
    def test_call_and_stubbed_response(self, mocked_requests_get):
        mocked_requests_get.return_value.json.return_value = {"foo": "bar"}
        call_single_endpoint()
        assert mocked_requests_get.called_once
        assert mocked_requests_get.return_value.json.return_value == {"foo": "bar"}

    @patch("requests.get")
    def test_call_and_response_different_values(self, mocked_requests_get):
        mocked_requests_get.return_value.json.side_effect = [
            {"fruit": "orange"},
            {"fruit": "apple"},
        ]
        first_result = call_single_endpoint()
        assert mocked_requests_get.return_value.json.call_count == 1
        assert first_result == {"fruit": "orange"}
        second_result = call_single_endpoint()
        assert second_result == {"fruit": "apple"}
        assert mocked_requests_get.return_value.json.call_count == 2
