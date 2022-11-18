### N o T e S

---

Xss injection --> <script> alert `xss` </script>

Another basic XSS Injection :

```js
<script>alert("flag")</script>
```

---

Reflected XSS

```py
Reflected XSS is a kind of cross-site scripting attack, where malicious script is injected into websites that are trusted or otherwise benign.
```

#### Directory Traversal 

```py
cd ../../..;pwd;
cd ../..;ls -al;pwd;

#Vulnerable to command injection
```
