### N o T e S : 

---

Cross site scripting (XSS) - It is a type of security vulnerability typically found in web applications. XSS attacks enable attackers to inject client-side scripts into web pages
viewed by other users.

```py
An XSS vulnerability may be used by attackers to bypass access controls such as same origin policy.
```

Example : 
```py
Xss injection --> <script> alert xss </script>
```

---

### Stored XSS attack

Injected malicious script is stored on the target server. Then the victim will retrieve some contents including the injected script.  
#### With the succesful XSS attack : 

- arbitrary file reading
- Malware installation
- changing URLs or contents of the web browser
- One can steal user's credentials as well
- including session cookies

---

### Reflected XSS Attack

Malicious script in the request is directly embedded to the response. It can be a part of the request URL.

Example : 
```py 
https://search.service/?query=%3Cscript%3Econsole.log(%22BAD%22);%3C/script%3Ebad 
```
(Because the script part is recognized as a HTML tag,
it won’t be displayed on the screen.)

The JavaScript code in the query string will work on the victim’s web browser.

---

### DOM-BASED XSS Attack

Malicious code is dynamically injected to the DOM* environments.  
▪ by the JavaScript code on the web page.  
▪ It arises when a JavaScript in the web content executes or embeds untrusted data, such as the URL.  
▪ The server is not involved in the attack sequence.  
▪ DOM-Based XSS attack can be regarded as a sub class of reflected XSS attack.  
 
---



