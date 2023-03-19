# Local File Inclusion (LFI)

- Local File Inclusion is an attack technique in which attackers trick a web application into either running or exposing files on a web server.

- Example of lfi vulnerbale code

>$file = $_GET['file'];
>
>include('directory/' . $file);

## Impacts of LFI vulnerabilities

- The impact of a Local File Inclusion attack can vary based on the exploitation and the read permissions of the webserver user. Based on these factors, an attacker can gather usernames via an /etc/passwd file, harvest useful information from log files, or combine this vulnerability with other attack vectors (such as file upload vulnerability) to execute commands remotely.



## Preventing LFI

- To avoid LFI and many other vulnerabilities, never trust user input. If you need to include local files in your website or web application code, use a whitelist of allowed file names and locations. Make sure that none of these files can be replaced by the attacker using file upload functions.


## Attack scenario

In our page we got same thing but with page variable or query for example survey page

> http://ipaddress/?page=survey

We can try and go out of the root folder of the website and acces sensible data like /etc/passswd
as start:
> http://ipaddress/?page=../etc/passwd
nothing happened . So we will add ../ till we got a result

- finally:
    > http://ipaddress/?page=../../../../../../../../etc/passwd

    worked and we got the flag !

