### LCG

---

Random no. generator.

### Pem files

```py
ssh-keygen -f private.pem -y | xclip
ssh-keygen -f private.pem -y > public.pub
chmod 400 private.pem
```

<!--from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode
from Crypto.Util.number import *

key64 = 'MIICITANBgkqhkiG9w0BAQEFAAOCAg4AMIICCQKCAgACnR8r4GemZPmX2+zLsBgzqHanMd0pbEGFRRldNezYX9A3HT99peociEbEMUnUaVWuDbzHJX7drG8s/exQW4XFfE5lGy+D0gSkJfQS1komUxic6iWH/1bZnU6rWFJlpbIzy/3IMx4QIx5cbOA0SsLuAomMEi4ZERGLxm2ta7ZZZuEYVYIa9/mrlXYkTgi1fxLguT35ykHNk5Rm8e8Q8KF/V2pQ3CQIQYZra2WLGNsxOXW7FLttmMyzgi4WQjLE/SVMs7Th5lGkjmXoQpMcc0ZhkL3H0vMHWtQeclqsE+QXgAUQFshiSb0auf69y/H+R+qJCO0jRgBz3OVudSx91oSBGaF7DTfFu3LsgJvMDRAdhPgdlLLzlR0PldVq1jKwjs1dWce2R5r4B0dnXqPrxLuuA/WNp3ni3jp6AL2y7MKn2AylPUEr+/fQ6+B33wuIHcZiXHdYYPvemehtCf1WCV4Q/C10Q3E6PK6R+dncE7ZUg0U3qnA84rAZUwweGLUD2yXngHMxDLLRv44Uv28XFvl35kFrlJhIhxtx/Fon70EKNboDCT8UXJ5ZlMyt47WBmYGp7FZbafbH6coLAQr1LQCyHCJYimu7lXr9eGYixE93xXHJ3KIJPaZGmhW3qbj3B8ZxrIvGjkZtHqiw+OCNj343Q44DknQ8F3CwBmZUmBxZSQIDAQAB'

keyDER = b64decode(key64)
keyPub = RSA.importKey(keyDER)
print(keyPub)
print(bytes_to_long(keyDER))-->
