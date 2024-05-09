import requests


def send_request(url, method, data=None, token=None):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    if token:
        headers['Authorization'] = f'Bearer {token}'

    if method.upper() == 'GET':
        response = requests.get(url, headers=headers, params=data)
    elif method.upper() == 'POST':
        response = requests.post(url, headers=headers, json=data)
    else:
        raise ValueError(f'Unsupported method: {method}')

    response.raise_for_status()

    return response.json()
