from unittest.mock import patch
from python_mocking import call_single_endpoint, call_post_endpoint, call_post_endpoint_with_data


@patch("requests.get")
def test_call_single_endpoint_mock(mocked_requests_get):
    call_single_endpoint()
    assert mocked_requests_get.called_once


def test_call_single_endpoint_mock_without_decorator():
    with patch("requests.get") as mocked_requests_get:
        call_single_endpoint()
        assert mocked_requests_get.called_once


def test_call_single_endpoint_mock_with_mocker_param(mocker):
    mocked_requests_get = mocker.patch("requests.get")
    call_single_endpoint()
    assert mocked_requests_get.called_once


class TestRequests:
    @patch("requests.get")
    def test_call_and_stubbed_response(self, mocked_requests_get):
        mocked_requests_get.return_value.json.return_value = {"foo": "bar"}
        call_single_endpoint()
        assert mocked_requests_get.called_once
        assert mocked_requests_get.return_value.json.return_value == {
            "foo": "bar"}

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

    @patch("requests.post")
    def test_call_post_endpoint(self, mocked_requests_post):
        mocked_requests_post.return_value.json.return_value = {"foo": "bar"}
        call_post_endpoint()
        assert mocked_requests_post.called_once
        assert mocked_requests_post.return_value.json.return_value == {
            "foo": "bar"}

    @patch("requests.post")
    def test_call_post_endpoint_with_data(self, mocked_requests_post):
        mocked_requests_post.return_value.json.return_value = {"foo": "bar"}
        call_post_endpoint_with_data({"userId": 2})
        second_param_of_call = mocked_requests_post.call_args[0][1]
        assert mocked_requests_post.called_once
        assert second_param_of_call == {"userId": 2}
