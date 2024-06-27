### JSON Web tokens

---

JSON web tokens (JWTs) are a standardized format for sending cryptographically signed JSON data between systems. Use - authentication, session handling, and access control mechanisms.

Task : We need to generate a JWT token having an admin role instead of having a user. Finding the key used to sign is important otherwise the signature for a different payload won't be correct.

Sometimes the JWT is encrypted with some hashing algorithm, we need to break it using 'john the ripper' or other bruteforcing tool and reconstruct the jwt.

```py
% jwt-cracker -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzA5OTMzODUzfQ.aDP5hVVQQN2uFQL15oTBG1B83j8MnQu0f7IRxodKm24 -d wordlists/rockyou.txt
john jwt.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256

SECRET FOUND: banana
Time taken (sec): 0.123
Total attempts: 20000
```
