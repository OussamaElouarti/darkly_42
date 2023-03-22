# Survey


## Attack scenario

We got a page with grade input between 1-10 lets intrcept the page with burpsuite and try to send a request with a value higher than 10 or lower than 1
And we got the flag 

To avoid vulns like this we need to parse the value in the backend and not trust client input.
