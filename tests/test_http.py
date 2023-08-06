from python_mocking import call_single_endpoint


def test_call_single_endpoint_mock(mocker):
    mocked_http_client = mocker.patch("requests.get")
    call_single_endpoint()
    assert mocked_http_client.called


def test_call_and_stubbed_response(mocker):
    mocked_http_client = mocker.patch("requests.get")
    mocked_http_client.return_value.json.return_value = {"foo": "bar"}
    call_single_endpoint()
    assert mocked_http_client.called
    assert mocked_http_client.return_value.json.called
    assert mocked_http_client.return_value.json.return_value == {"foo": "bar"}
