# XSS FEEDBACK

XSS or cross site scripting  allows an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform, and to access any of the user's data. If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application's functionality and data.

Typical XSS attacks include session stealing, account takeover, MFA bypass, DOM node replacement or defacement, attacks against the user’s browser such as malicious software downloads, keylogging, and other client-side attacks.

we can get the flag simply by entring script or alert in message or name inputs

To avoid xss probelm we need to sanitize the client input and never trust it

## Preventing XSS flaws 

Preventing XSS requires the separation of untrusted data from active browser content. This can be achieved by:

    - Using frameworks that automatically escape XSS by design, such as the latest Ruby on Rails or React JS. Learn the limitations of each framework’s XSS protection and appropriately handle the use cases which are not covered.

    - Escaping untrusted HTTP request data based on the context in the HTML output (body, attribute, JavaScript, CSS, or URL) will resolve Reflected and Stored XSS vulnerabilities .

    - Applying context-sensitive encoding when modifying the browser document on the client side acts against DOM XSS. When this cannot be avoided, similar context-sensitive escaping techniques can be applied to browser APIs .

    - Enabling a Content Security Policy (CSP) as a defense-in-depth mitigating control against XSS. It is effective if no other vulnerabilities exist that would allow placing malicious code via local file includes
