import asyncio
import aiohttp
from azure.identity.aio import ClientSecretCredential

# Azure AD App Credentials
tenant_id = "<Tenant-id>"
client_id = "<Client-id>"
client_secret = "<client-secret>"

# Create token lifetime policy
async def create_token_lifetime_policy():
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    token = await credential.get_token("https://graph.microsoft.com/.default")

    url = "https://graph.microsoft.com/v1.0/policies/tokenLifetimePolicies"
    headers = {
        "Authorization": f"Bearer {token.token}",
        "Content-Type": "application/json"
    }

    payload = {
        "definition": [
            "{\"TokenLifetimePolicy\":{\"Version\":1,\"AccessTokenLifetime\":\"23:00:00\"}}"
        ],
        "displayName": "24 Hour token policy",
        "isOrganizationDefault": False,
        "type": "TokenLifetimePolicy"
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            if response.status in [200, 201]:
                data = await response.json()
                print("✅ Policy created!")
                print(f"ID: {data['id']}")
            else:
                error = await response.text()
                print(f"❌ Failed to create policy. Status: {response.status}")
                print("Response:", error)

asyncio.run(create_token_lifetime_policy())
