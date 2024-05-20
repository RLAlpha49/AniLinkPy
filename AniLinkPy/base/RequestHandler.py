# pylint: disable=invalid-name
from typing import Optional

import requests

from AniLinkPy.exceptions import RequestError, UnsupportedMethodError


def send_request(
    url: str, method: str, data: dict, token: Optional[str] = None, timeout: int = 15
) -> dict:
    """
    This function sends a request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        method (str): The HTTP method to use for the request. Supports 'GET' and 'POST'.
        data (dict, optional): The data to include in the request. Defaults to None.
        token (str, optional): The authentication token. Defaults to None.
        timeout (int, optional): The number of seconds the client will wait for the server to send a response.

    Raises:
        UnsupportedMethodError: If an unsupported method is provided.
        RequestError: If there is an error in the request response.

    Returns:
        dict: The JSON response from the request.
    """
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if method.upper() not in ["GET", "POST"]:
        raise UnsupportedMethodError(method)

    response = None

    if method.upper() == "GET":
        response = requests.get(url, headers=headers, params=data, timeout=timeout)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, json=data, timeout=timeout)

    if response is None:
        raise RequestError("No response received")

    if response is not None:
        response_json = response.json()
        if "errors" in response_json and response_json["errors"]:
            raise RequestError(response_json["errors"])

    return response.json()
