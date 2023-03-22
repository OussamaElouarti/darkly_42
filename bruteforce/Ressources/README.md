# Brute Force user

Brute force attacks utilise automated techniques such as credential stuffing and card cracking, continually testing large quantities of information on a website to gain entry to a user’s account.

## impacts of Brute Force attacks

- **Identity theft** : stealing someone’s identity to access their accounts, such as bank accounts or credit cards. This enables the attacker to purchase goods using these details. In addition, information such as social security numbers can be sold for use in other cyber attacks.

- **Loss of data** : due to loss of confidentiality if data is stolen which could destroy company reputation. Additionally, there may be reputational damage caused by a leak of sensitive customer information that leads to public distrust and dissatisfaction with the business.

- **Downtime** : this refers to system outages where websites or computer networks cannot be accessed due to a cyber attack. This is costly to the business in terms of lost revenue, customer satisfaction as well as loss of image.


## preventing Brute Force attacks

- Use strong and unique passwords :
    - Avoid using common words or personal information in your passwords, as they can be easily guessed.
    - Ignore the most common passwords.  
    - Implement policies to reject weak passwords and enforce users to change their passwords frequently.

- Enable multi-factor authentication (MFA)

- Limit the number of login attempts made within a certain period and lock down the account after a certain number of login attempts.

- Use CAPTCHA : a CAPTCHA can determine whether the user is a human or a computer. we can make it more difficult for automated brute-force attacks to succeed by requiring users to complete a CAPTCHA before attempting to log in.


## attack scenario

- We got a user in members that had a surname GetThe and first name Flag its a bit sus

so we will try to brute force this user in signin page using burpsuite intruder with rockyou.txt wordlist

after waiting for sometime we got shadow as password we try it in sigin page and it works!


