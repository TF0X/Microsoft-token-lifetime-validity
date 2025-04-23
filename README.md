# Microsoft-token-lifetime-validity
A bunch of script used to create a microsodt lifetime token policy to assign to app princippal for the puropse of incresing lifespan of bearer token upto 24 hours. 
Use case for this policy if you want to use bearer token to access clooud resources they will expire by default in a 60 minutes causing workload to be interrupted 
in a nutshell this can be used to increase the lifetime of microsft token.


1. Create.py to create a token lifetime vailidty (is token lifetime validity : true/false) this setting is used to apply tenant wide if applied doesnt need to apply next steps
2. get.py list all the lifetime policy created
3. delete.py delete the poicies that re already created
4. assign.py assign policy to a app registration (only works if policy is not tenant wide ) also a litlle buggy 

token lifetime is in preview 

https://learn.microsoft.com/en-us/graph/api/resources/tokenlifetimepolicy?view=graph-rest-1.0
https://learn.microsoft.com/en-us/graph/api/application-post-tokenlifetimepolicies?view=graph-rest-1.0
