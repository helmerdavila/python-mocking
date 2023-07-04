import pytest
from python_mocking import call_single_endpoint


def test_call_single_endpoint_mock(mocker):
    mocked_http_client = mocker.patch("requests.get")
    call_single_endpoint()
    assert mocked_http_client.called
