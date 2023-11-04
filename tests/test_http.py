from unittest.mock import patch, call
from python_mocking import (
    call_single_endpoint,
    call_post_endpoint,
    call_post_endpoint_with_data,
    posts_url,
    todos_single_url,
)


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


@patch("requests.post")
def test_assert_called_with(mocked_requests_post):
    data = {"userId": 3}
    call_post_endpoint_with_data(data)
    mocked_requests_post.assert_called_with(posts_url, data)


@patch("requests.post")
def test_assert_called_once_with(mocked_requests_post):
    data = {"userId": 3}
    call_post_endpoint_with_data(data)
    mocked_requests_post.assert_called_once_with(posts_url, data)


class TestRequests:
    @patch("requests.get")
    def test_call_and_stubbed_response(self, mocked_requests_get):
        mocked_requests_get.return_value.json.return_value = {"foo": "bar"}
        call_single_endpoint()
        assert mocked_requests_get.called_once_with(todos_single_url)
        assert mocked_requests_get.return_value.json.return_value == {"foo": "bar"}

    @patch("requests.get")
    def test_call_args(self, mocked_requests_get):
        call_single_endpoint()
        assert mocked_requests_get.call_args == call(todos_single_url)

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
        assert mocked_requests_post.return_value.json.return_value == {"foo": "bar"}

    @patch("requests.post")
    def test_call_post_endpoint_with_data(self, mocked_requests_post):
        mocked_requests_post.return_value.json.return_value = {"foo": "bar"}
        call_post_endpoint_with_data({"userId": 2})
        second_param_of_call = mocked_requests_post.call_args[0][1]
        assert mocked_requests_post.called_once
        assert second_param_of_call == {"userId": 2}
