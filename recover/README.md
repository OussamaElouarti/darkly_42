# password recover

in signin page we got "I forget my password" link

after clicking it we got a page with submit button lets inspect the page

we found a hidden mail input with webmaster@borntosec.com mail lets try and change it and send the request with submit button

> THE FLAG IS : 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

To avoid this type of vulns we need to parse the email in backend and add an if statment to reject any other email.
