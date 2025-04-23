import asyncio
from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient

# Azure AD App Credentials
tenant_id = "<tenant-id>"
client_id = "<Client-id>"
client_secret = "<Secret>"

# Authenticate
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
graph_client = GraphServiceClient(credential, scopes=["https://graph.microsoft.com/.default"])

# Get all token lifetime policies
async def get_all_token_lifetime_policies():
    try:
        response = await graph_client.policies.token_lifetime_policies.get()
        
        if response.value:
            print("📋 List of Token Lifetime Policies:")
            for policy in response.value:
                print(f"\n🔹 Policy Name: {policy.display_name}")
                print(f"🆔 ID: {policy.id}")
                print(f"📝 Definition: {policy.definition}")
                print(f"🏢 Default: {'Yes' if policy.is_organization_default else 'No'}")
        else:
            print("ℹ️ No token lifetime policies found.")
            
        return response.value
        
    except Exception as e:
        print(f"❌ Error fetching policies: {str(e)}")
        return None

# Run
asyncio.run(get_all_token_lifetime_policies())
