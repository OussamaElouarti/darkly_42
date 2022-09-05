As a first step for a pentester is to check for directories and files in website one of them is robots.txt

```Robots.txt is a text file with instructions for search engine crawlers. It defines which areas of a website crawlers are allowed to search. However, these are not explicitly named by the robots.txt file. Rather, certain areas are not allowed to be searched. Using this simple text file, you can easily exclude entire domains, complete directories, one or more subdirectories or individual files from search engine crawling. However, this file does not protect against unauthorized access.```

robots.txt :
> User-agent: *
> 
>Disallow: /whatever
>
>Disallow: /.hidden


In whatever directory we got a file called htpasswd its on the same directory of this readme file

>root:437394baff5aa33daa618be47b75cb49

we tried it in sigin page no result after searching I found an admin page
the password is an md5 after decryption we got qwerty123@

worked in the adim page 

>The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff

To avoid this problem
tryin to dissalow a specific file in robots.txt makes it look sus for hackers
So you need to give access in webserver to this file to admins only.
