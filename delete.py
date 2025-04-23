import asyncio
from azure.identity.aio import ClientSecretCredential
import aiohttp

# === Azure Credentials ===
tenant_id = "<Tenant-id>"
client_id = "<client-id>"
client_secret = "<client-secret>"

# === Token Lifetime Policy ID to delete ===
policy_id = '<policy-id>'  # 🔁 Replace with the actual policy ID you want to delete

async def delete_policy():
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    token = await credential.get_token("https://graph.microsoft.com/.default")

    headers = {
        "Authorization": f"Bearer {token.token}",
        "Content-Type": "application/json"
    }

    delete_url = f"https://graph.microsoft.com/v1.0/policies/tokenLifetimePolicies/{policy_id}"

    async with aiohttp.ClientSession() as session:
        async with session.delete(delete_url, headers=headers) as response:
            if response.status == 204:
                print("🗑️ Token Lifetime Policy deleted successfully from tenant!")
            else:
                error = await response.text()
                print(f"❌ Failed to delete policy. Status: {response.status}")
                print("Response:", error)

asyncio.run(delete_policy())
