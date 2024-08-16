import requests

def get_access_token(client_id, client_secret, username, password):
    url = "https://services.govwin.com/neo-ws/oauth/token"

    payload = {
        "grant_type": "password",
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password,
        "scope": "read"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        token_info = response.json()
        return token_info["access_token"]
    else:
        print(f"Error: Unable to fetch access token")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# enter info here
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

access_token = get_access_token(client_id, client_secret, username, password)
if access_token:
    print(f"Access Token: {access_token}")
