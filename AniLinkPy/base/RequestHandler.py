"""
This module contains the send_request function which is used to send HTTP requests.
"""

# pylint: disable=invalid-name
import requests


def send_request(url, method, data=None, token=None, timeout=15) -> dict:
    """
    This function sends a request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        method (str): The HTTP method to use for the request. Supports 'GET' and 'POST'.
        data (dict, optional): The data to include in the request. Defaults to None.
        token (str, optional): The authentication token. Defaults to None.
        timeout (int, optional): The number of seconds the client will wait for the server to send a response.

    Raises:
        ValueError: If an unsupported method is provided.

    Returns:
        dict: The JSON response from the request.
    """
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if method.upper() == "GET":
        response = requests.get(url, headers=headers, params=data, timeout=timeout)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, json=data, timeout=timeout)
    else:
        raise ValueError(f"Unsupported method: {method}")

    response.raise_for_status()

    return response.json()
