### CSRF

---

It happens when an attack can trick a victim in going to a page controlled by hacker.

```py
For a CSRF attack to be possible, three key conditions must be in place:

A relevant action. There is an action within the application that the attacker
 has a reason to induce. This might be a privileged action (such as modifying permissions
 for other users) or any action on user-specific data (such as changing the user's own password).

Cookie-based session handling. Performing the action involves issuing one or more HTTP
 requests, and the application relies solely on session cookies to identify the user
 who has made the requests. There is no other mechanism in place for tracking sessions
 or validating user requests.

No unpredictable request parameters. The requests that perform the action do not contain
 any parameters whose values the attacker cannot determine or guess. For example, when
causing a user to change their password, the function is not vulnerable if an attacker needs
 to know the value of the existing password.
```



