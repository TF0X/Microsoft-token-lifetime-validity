import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient
from msgraph.generated.models.reference_create import ReferenceCreate

# === Configuration ===
tenant_id = '<tenant-id>'
client_id = '<client-id>'
client_secret = '<client-secret>'

# === Token Policy and Target App Registration ===
application_id = '<Object-id>'   # <- App you want to assign policy to (objectId, not clientId)
policy_id = '<ploicy-id>'  # <- Your token policy ID

async def assign_policy():
    # 1. Authenticate and initialize Graph client
    credential = ClientSecretCredential(tenant_id, client_id, client_secret)
    graph_client = GraphServiceClient(credential, scopes=["https://graph.microsoft.com/.default"])

    # 2. Create ReferenceCreate object with the policy URI
    request_body = ReferenceCreate(
        odata_id=f"https://graph.microsoft.com/v1.0/policies/tokenLifetimePolicies/{policy_id}"
    )

    # 3. Assign the policy to the app
    try:
        await graph_client.applications \
            .by_application_id(application_id) \
            .token_lifetime_policies \
            .ref \
            .post(request_body)

        print(f"✅ Token Lifetime Policy {policy_id} assigned to Application {application_id}.")
    except Exception as e:
        print(f"❌ Failed to assign policy: {e}")

# Run
asyncio.run(assign_policy())
