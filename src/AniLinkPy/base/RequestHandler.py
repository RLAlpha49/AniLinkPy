import requests


def send_request(url, method, data=None, token=None):
    """
    This function sends a request to the specified URL.

    Args:
        url (str): The URL to send the request to.
        method (str): The HTTP method to use for the request. Supports 'GET' and 'POST'.
        data (dict, optional): The data to include in the request. Defaults to None.
        token (str, optional): The authentication token. Defaults to None.

    Raises:
        ValueError: If an unsupported method is provided.

    Returns:
        dict: The JSON response from the request.
    """
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if method.upper() == "GET":
        response = requests.get(url, headers=headers, params=data)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, json=data)
    else:
        raise ValueError(f"Unsupported method: {method}")

    response.raise_for_status()

    return response.json()
