#Token Lifetime Policy Management Scripts for Microsoft Identity Platform

This set of Python scripts helps manage Token Lifetime Policies for Azure AD applications. The primary goal is to extend the lifespan of bearer tokens (up to 24 hours), which is especially useful for long-running workloads that rely on token-based authentication to access cloud resources.

By default, Microsoft bearer tokens expire after 60 minutes, which can interrupt operations. These scripts allow you to create, assign, list, and delete token lifetime policies to help mitigate that.

    ⚠️ Token Lifetime Policies are currently in preview. Refer to the official Microsoft documentation for the latest details.

📁 Script Overview
create.py

    Purpose: Creates a token lifetime policy.

    Usage: Used to define a custom policy for token validity duration.

    Special Note: You can also apply the policy tenant-wide using the isOrganizationDefault setting.
    If this is enabled (true), you do not need to assign the policy to individual applications.

get.py

    Purpose: Lists all token lifetime policies in your tenant.

    Usage: Useful for auditing or identifying existing policies.

delete.py

    Purpose: Deletes one or more token lifetime policies.

    Usage: Clean up unused or misconfigured policies.

assign.py

    Purpose: Assigns a policy to a specific App Registration (Service Principal).

    Limitations:

        Only works if the policy is not tenant-wide.

        This script is experimental and may have minor bugs.

🔗 Resources

    Microsoft Graph: TokenLifetimePolicy Resource Type

    Assign TokenLifetimePolicy to an Application

🚧 Disclaimer

Token Lifetime Policies are in preview and subject to change. Always test in non-production environments before deploying widely.
