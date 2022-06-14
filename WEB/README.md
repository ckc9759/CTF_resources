### Hi guys,

Now, here's my basic methodology... It's over simplified for hard stuff, but is very useful for someone who is doing basic web things. 
```
* Step 1: Open up Chrome Dev Tools

* Step 2: Use the site as intended

* Step 3: See what happens. 
```


While playing around, check out these basic tips for finding weirdness.



#### Dummy Stuff
```
Find all login pages
Many bugs, however complicated their root cause might be, display themselves as a normal user having powers that were meant only for admin
Generally, anything that "admin" is the only group allowed to do that "user" has access to is considered bad. Test everything, attack admin functionality as a normally priv'd user.
If you see the word admin, you're probably on the right track.
Also, always try admin:admin on everything you touch.
As a near general rule, you will not bruteforce logins during CTFs, so don't do it without permission from organizers. If you are bruteforcing, you are likely wrong.
```


### What else to look for
```python
1. buggy phps
2. sensitive data exposure
3. Injection attacks (SQL)
4. Cross site scripting (XSS)
5. Poor coding or site maintainence (cookies or source code or bin files or even robots.txt)
6. Broken authentication
7. Inclusion vulnerabilities
8. version control artifacts
```

### Useful
```
wireshark/tcpdump to check for packets
ngrep to search for string in packet capture
Burpsuite
Use curl sometimes to get the webpage in command line
```

#### Find all upload/content send mechanisms
```
View source of pages
Check out cookies (base 64/ plaintext)
The most common way sessions are maintained is with cookies.
Always check the cookies on a web page, either with a cookie editing tool or using browser DevTools
Cookies can be (Will be) encoded so don't be discouraged if they are random alphanumerics, always make sure to check Base64 and other common encodings.
Look at URLs
If the URL looks like it has a number at the end, try incrementing the number.
If the URL has your username at the end, change the username.
Look for Robots.txt
Attack login pages
try baby SQL inject on each one
try baby command inject on each one
Attack input pages
try baby command inject on each one
run an XSS scan
```
#### Recon
```
Nmap -A
Services on weird ports are common
Dirbust for 2 minutes if nothing against it.
Admin panels might pop up
Vuln scan with Nikto. If you have a real commercial one, hit it, but you probably won't find anything. CTF challenges aren't supposed to be solved by a scanner.
Always remember to use cheatsheets: 
```
https://github.com/OWASP/CheatSheetSeries/tree/master/cheatsheets

Fake it from there.

#### Latex injection
```
Sometimes, web challenges have latex injection where it render something when you type. To cract it you can use \input{/etc/passwd} or something as the question suggests.
```
