from python_mocking import call_single_endpoint


def test_call_single_endpoint_mock(mocker):
    mocked_http_client = mocker.patch("requests.get")
    call_single_endpoint()
    assert mocked_http_client.called_once


def test_call_and_stubbed_response(mocker):
    mocked_http_client = mocker.patch("requests.get")
    mocked_http_client.return_value.json.return_value = {"foo": "bar"}
    call_single_endpoint()
    assert mocked_http_client.called
    assert mocked_http_client.return_value.json.call_count == 1
    assert mocked_http_client.return_value.json.return_value == {"foo": "bar"}


def test_call_and_response_different_values(mocker):
    mocked_http_client = mocker.patch("requests.get")
    mocked_http_client.return_value.json.side_effect = [
        {"fruit": "orange"}, {"fruit": "apple"}]
    first_result = call_single_endpoint()
    assert mocked_http_client.called
    assert mocked_http_client.return_value.json.call_count == 1
    assert first_result == {"fruit": "orange"}
    second_result = call_single_endpoint()
    assert second_result == {"fruit": "apple"}
    assert mocked_http_client.return_value.json.call_count == 2
