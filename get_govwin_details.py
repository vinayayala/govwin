
import requests

def get_opportunity_details(govwin_id, access_token):
    # url to access api
    base_url = "https://services.govwin.com/neo-ws/opportunities"

    # gets opportunity details
    url = f"{base_url}/{govwin_id}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        contract_value = data.get("oppValue")
        solicitation_date = data.get("solicitationDate", {}).get("value")
        requirements = data.get("primaryRequirement")

        # return details
        return {
            "Contract Value": contract_value,
            "Solicitation Date": solicitation_date,
            "Requirements": requirements
        }
    else:
        # error catching
        print(f"Error: Unable to fetch details for GovWin ID {govwin_id}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return None

# enter ID and access token
govwin_id = "YOUR_GOVWIN_ID"
access_token = "YOUR_ACCESS_TOKEN"

details = get_opportunity_details(govwin_id, access_token)
if details:
    print(details)
