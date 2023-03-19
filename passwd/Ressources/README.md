# admin(htpasswd)

## Attack scenario

As a first step for a pentester is to check for directories and files in website one of them is robots.txt

```Robots.txt is a text file with instructions for search engine crawlers. It defines which areas of a website crawlers are allowed to search. However, these are not explicitly named by the robots.txt file. Rather, certain areas are not allowed to be searched. Using this simple text file, you can easily exclude entire domains, complete directories, one or more subdirectories or individual files from search engine crawling. However, this file does not protect against unauthorized access.```

### robots.txt :
> User-agent: *
> 
>Disallow: /whatever
>
>Disallow: /.hidden


In whatever directory we got a file called htpasswd its on the same directory of this readme file

>root:437394baff5aa33daa618be47b75cb49

we tried it in sigin page no result. after searching we found an admin page
the password is an md5 after decryption we got qwerty123@

It worked in the admin page 

## Preventing robots.txt vulnerability 

- The robots.txt file can be viewed by anyone, and it might contain sensitive information about the server. For example, specifying which directories shouldn't be indexed tells the attacker where the sensitive files are.