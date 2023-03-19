# headers

## Attack scenario

In the footer of the home page there is a link © BornToSec

We inspect the page we got some comments at the end of the page

> You must come from : "https://www.nsa.gov/".

>	Let's use this browser : "ft_bornToSec". It will help you a lot.

We need to change the headers in the request to do that we sent a request using curl and changed referer header to "https://www.nsa.gov/
and User-Agent to ft_bornToSec

the request is now like this :

> curl http://10.12.176.141/\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f 
> -H "Referer: https://www.nsa.gov/" 
> -H "User-Agent: ft_bornToSec"


and got the flag!
