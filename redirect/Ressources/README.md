# Bad Redirect

Unvalidated redirects are possible when a web application accepts untrusted input that could cause the web application to redirect the request to a URL contained within untrusted input. By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials.


## Attack scenario

In the footer of the home page there is 3 icon media with redirection to each social media

If we inspect the icons :

> href="index.php?page=redirect&site=instagram"

> href="index.php?page=redirect&site=facebook"

> href="index.php?page=redirect&site=twitter"

lets try to change social media name for example

> href="index.php?page=redirect&site=google"

We get redirect to a page with the flag

> GOOD JOB HERE IS THE FLAG : B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3

## impacts of Unvalidated redirects 

- Open redirection attacks are most commonly used to support phishing attacks, or redirect users to malicious websites.



## preventing Unvalidated Redirects

- Simply avoid using redirects.

- If used, do not allow the URL as user input for the destination.

- If user input can’t be avoided, ensure that the supplied value is valid, appropriate for  the application, and is authorized for the user

- Sanitize input by creating a list of trusted URLs (lists of hosts or a regex).
    - This should be based on an allow-list approach, rather than a block list.

- Force all redirects to first go through a page notifying users that they are going off of your site, with the destination clearly displayed, and have them click a link to confirm.