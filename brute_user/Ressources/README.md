# Brute force user

We got a user in members that had a surname GetThe and first name Flag its a bit sus

so we will try to brute force this user in signin page using burpsuite using intruder with rockyou.txt wordlist

after waiting for sometime we got shadow as password we try it in sigin page and it works!

>THE FLAG IS : B3A6E43DDF8B4BBB4125E5E7D23040433827759D4DE1C04EA63907479A80A6B2

We can avoid this vulnerablity by 
 -a strong password that doesnt belong in any wordlist
 
 -we can use 2fa
 
 -lockout account after certain attempts 
